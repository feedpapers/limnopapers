import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from limnopapers import *
import feedparser
import pandas as pd

url = "https://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=10021&channel-name=Ecosystems"
posts = []

feed = feedparser.parse(url)
for post in feed.entries:
    posts.append(post)

res = pd.DataFrame(posts)
try:
    if(len(set(list(res.columns)). \
           intersection(['title', 'link', 'published'])) != 3):
        raise ValueError('Missing Field')
except:
    if(len(set(list(res.columns)). \
           intersection(['title', 'link', 'updated'])) != 3):
        raise ValueError('Missing Field')

res.to_csv("test.csv")

res = filter_limno(res)
toots = res['title'] + ". " + res['link']

for toot in toots:
    print(toot)
