import feedparser
import pandas as pd
import datetime
import twitter

def filter_limno(df):
    mentions_limno = df['summary'].str.contains('lake')
    mentions_junk = df['summary'].str.contains('ocean')
    return(df.drop(df[mentions_limno == False & mentions_junk].index.values))

def filter_today(df, day):
    published_today = (df['updated'] > datetime.datetime.strptime(day, "%Y-%m-%d") - datetime.timedelta(days = 1)) & (df['updated'] < datetime.datetime.strptime(day, "%Y-%m-%d") + datetime.timedelta(days = 1))     
    return(df.drop(df[published_today == False].index.values))

def get_papers(day = str(datetime.date.today())):
    # https://stackoverflow.com/questions/45701053/get-feeds-from-feedparser-and-import-to-pandas-dataframe
    rawrss = [
        'http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1939-5590',
        'http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)2378-2242'
        ]

    posts = []
    for url in rawrss:
        feed = feedparser.parse(url)
        for post in feed.entries:
            posts.append((post.title, post.summary, post.prism_url, post.dc_source, post.updated))

    res = pd.DataFrame(posts, columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated'])
    res['updated'] = pd.to_datetime(res['updated'])
    res = res.sort_values(by = ['updated'])
    res = filter_limno(res)
    res = filter_today(res, day)
    # res.to_csv("test.csv")

    return(res)

def limnotoots(event, context):
    api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='',	access_token_secret='')

    data = get_papers()    
    
    toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']    
    
    for toot in toots:
        status = api.PostUpdate(toot)        

