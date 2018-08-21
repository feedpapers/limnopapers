import feedparser
import pandas as pd
import datetime
import twitter
import sys
import config

def filter_limno(df):
    filter_for = ['lake', "reservoir"] 
    mentions_limno = df['title'].str.contains('|'.join(filter_for), case = False)

    filter_against = ['ocean']
    mentions_junk = df['summary'].str.contains('|'.join(filter_against))
    
    return(df.drop(df[mentions_limno == False & mentions_junk].index.values))

def filter_today(df, day):
    today_parsed = datetime.datetime.strptime(day + " 15:00:00", "%Y-%m-%d %H:%M:%S") 
    yesterday = today_parsed - datetime.timedelta(days = 0.5)
    tomorrow = today_parsed + datetime.timedelta(days = 0.5)
    published_today = (df['updated'] > yesterday) & (df['updated'] < tomorrow)
    return(df.drop(df[published_today == False].index.values))

def get_posts(day = str(datetime.date.today())):
    # https://stackoverflow.com/questions/45701053/get-feeds-from-feedparser-and-import-to-pandas-dataframe
    rawrss = pd.read_csv("journals.csv")["rawrss"].tolist()
    
    posts = []
    for url in rawrss:
        feed = feedparser.parse(url)
        for post in feed.entries:
            posts.append((post.title, post.summary, post.link, post.dc_source, post.updated))

    return(posts)

def get_papers(day = str(datetime.date.today()), to_csv = False):
    posts = get_posts(day = day)
    res = pd.DataFrame(posts)
    res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
    res['updated'] = pd.to_datetime(res['updated'])
    res = res.sort_values(by = ['updated'])
    if to_csv is not False:
      res.to_csv("test.csv")  
    res = filter_limno(res)
    res = filter_today(res, day)    

    return(res)

def limnotoots(day = str(datetime.date.today())):    
    api = twitter.Api(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret, access_token_key=config.access_token_key, access_token_secret=config.access_token_secret)        
    # print(api.VerifyCredentials())

    data = get_papers(day)        
    toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']    
    
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
