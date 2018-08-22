import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from limnopapers import *
import feedparser
import pandas as pd

url = "https://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=10533&channel-name=Biogeochemistry"
posts = []

feed = feedparser.parse(url)
for post in feed.entries:
    posts.append(post)    

res = pd.DataFrame(posts)
print(res.columns)
print(res['title'])
print(res['link'])
res.to_csv("test.csv")
