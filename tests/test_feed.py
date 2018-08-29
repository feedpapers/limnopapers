import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from limnopapers import *
import feedparser
import pandas as pd

url = "http://rss.sciencedirect.com/publication/science/03043800"
posts = []

feed = feedparser.parse(url)
for post in feed.entries:
    posts.append(post)    

res = pd.DataFrame(posts)
print(res.columns)
print(res['title'])
print(res['link'])
print(res['updated'])
res.to_csv("test.csv")
