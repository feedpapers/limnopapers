import pdb
import feedparser
import pandas as pd
import datetime
import twitter
import sys
import config


def filter_limno(df):

    df = df.reset_index()

    filter_for = ['lake', "reservoir", "inland waters"]
    has_limno_title = df['title'].str.contains('|'.join(filter_for),
                                               case = False)
    has_limno_summary = df['summary'].str.contains('|'.join(filter_for),
                                                   case = False)

    filter_against = ['ocean', 'iran', 'fault', 'wetland', 'correction',
                      'hydroelectric', '^mining$', 'Great Lakes', '^sea$']
    has_junk_summary = ~df['summary'].str.contains('|'.join(filter_against),
                                                   case = False)
    has_junk_title = ~df['title'].str.contains('|'.join(filter_against),
                                               case = False)

    is_limno = pd.DataFrame([has_limno_title, has_limno_summary,
                             has_junk_summary, has_junk_title]) \
        .transpose() \
        .sum(axis = 1) > 2

    return(df[is_limno])


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

    # sort rawrss by increasing journal name nchar length for pretty printing
    rawrss.index = rawrss['title'].str.len()
    rawrss = rawrss.sort_index().reset_index(drop = True)

    posts = []
    for i in range(len(rawrss.index)):
        sys.stdout.write('\b' * 1000)
        sys.stdout.write('Fetching papers from: ' + rawrss['title'][i] + '\r')

        single_posts = get_posts_(rawrss['title'][i], rawrss['rawrss'][i])
        posts.append(single_posts)

    print('\n')
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


def limnotoots(day = str(datetime.date.today()), interactive = False):
    api = twitter.Api(consumer_key=config.consumer_key,
                      consumer_secret=config.consumer_secret,
                      access_token_key = config.access_token_key,
                      access_token_secret=config.access_token_secret)
    # print(api.VerifyCredentials())

    data = get_papers(day)

    toots = data['title'] + ". " + data['dc_source'] + ". " + \
        data['prism_url']

    for toot in toots:
        print(toot)
        if(interactive is True):
            post_toot = input("post limnotoot (y)? ") or "y"
            if(post_toot in ["y"]):
                status = api.PostUpdate(toot)

                # write to log
                log = pd.read_csv("log.csv")
                keys = ["title", "dc_source", "prism_url"]

                title, dc_source, prism_url = toot.split(". ")
                d = dict(zip(keys, [title, dc_source, prism_url]))
                d = pd.DataFrame.from_records(d, index=[0])
                log = log.append(pd.DataFrame(data = d), ignore_index = True)
                log.to_csv("log.csv", index = False)
        else:
            status = api.PostUpdate(toot)

            # write to log
            log = pd.read_csv("log.csv")
            keys = ["title", "dc_source", "prism_url"]
            title, dc_source, prism_url = toot.split(". ")
            d = dict(zip(keys, [title, dc_source, prism_url]))
            d = pd.DataFrame.from_records(d, index=[0])
            log = log.append(pd.DataFrame(data = d))
            log.to_csv("log.csv", index = False)


def main():
    if(len(sys.argv) > 1):
        # yyyy-mm-dd format
        limnotoots(day = sys.argv[1], interactive = True)
    else:
        limnotoots()

if __name__ == "__main__":
    main()
