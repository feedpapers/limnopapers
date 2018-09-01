import feedparser
import pandas as pd
import datetime
import twitter
import sys
import config

def filter_limno(df):    
    filter_for = ['lake', "reservoir"]
    mentions_limno = df['title'].str.contains('|'.join(filter_for),
                                              case = False)
    df = df[mentions_limno]

    filter_against = ['ocean', 'iran', 'fault', 'wetland', 'correction',
                      'hydroelectric', 'mining']
    mentions_junk = df['summary'].str.contains('|'.join(filter_against),
                                               case = False)
    df = df[mentions_junk == False]

    return(df)

def filter_today(df, day):
    today_parsed = datetime.datetime.strptime(
        day + " 09:00:00", "%Y-%m-%d %H:%M:%S")
    yesterday = today_parsed - datetime.timedelta(days = 1)
    tomorrow = today_parsed + datetime.timedelta(days = 0)
    published_today = (df['updated'] > yesterday) & (df['updated'] < tomorrow)
    res_today = df[published_today]
    return(res_today)

def get_posts_(title, url):
    feed = feedparser.parse(url)
    posts = []
    for post in feed.entries:
        try:
            posts.append((post.title, post.summary, post.link,
                          title, post.updated))
        except AttributeError:
            posts.append((post.title, post.summary, post.link,
                          title, post.published))
    res = pd.DataFrame(posts)
    res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
    return(res)

def get_posts():
    # https://stackoverflow.com/questions/45701053/get-feeds-from-feedparser-and-import-to-pandas-dataframe
    rawrss = pd.read_csv("journals.csv")

    posts = []
    for i in range(len(rawrss.index)):
        print('Fetching papers from: ' + rawrss['title'][i])
        single_posts = get_posts_(rawrss['title'][i], rawrss['rawrss'][i])
        posts.append(single_posts)

    return(posts)

def get_papers(day = str(datetime.date.today()), limno = True, to_csv = False):
    posts = get_posts()
    res = pd.concat(posts)
    res['updated'] = pd.to_datetime(res['updated'])
    res = res.sort_values(by = ['updated'])
    res = res.drop_duplicates(subset = ['title'], keep = 'first')
    if limno is not False:
        res_limno = filter_limno(res)
    else:
        res_limno = res

    res_today = filter_today(res_limno, day)

    if to_csv is not False:
        res.to_csv("test.csv")
        res_limno.to_csv("test_limno.csv")
        res_today.to_csv("test_today.csv")

    # rm entries that are also in log
    log = pd.read_csv("log.csv")
    res_today = res_today[~res_today['title'].isin(log['title'])]

    return(res_today)

def limnotoots(day = str(datetime.date.today())):
    api = twitter.Api(consumer_key=config.consumer_key,
                      consumer_secret=config.consumer_secret,
                      access_token_key = config.access_token_key,
                      access_token_secret=config.access_token_secret)
    # print(api.VerifyCredentials())

    data = get_papers(day)

    # write to log
    log = pd.read_csv("log.csv")
    log = log.append(data)
    log.to_csv("log.csv")

    toots = data['title'] + ". " + data['dc_source'] + ". " + \
        data['prism_url']

    for toot in toots:
        print(toot)
        status = api.PostUpdate(toot)

def main():
    if(len(sys.argv) == 2):
        # yyyy-mm-dd format
        limnotoots(day = sys.argv[1])
    else:
        limnotoots()

if __name__ == "__main__":
    main()
