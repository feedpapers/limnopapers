import os
import sys
import inspect
import feedparser
import pandas as pd

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from limnopapers import *

url = "http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)2169-8961"
posts = []

feed = feedparser.parse(url)
for post in feed.entries:
    posts.append(post)

res = pd.DataFrame(posts)
try:
    if(len(set(list(res.columns)).
           intersection(['title', 'link', 'published'])) != 3):
        raise ValueError('Missing Field')
except:
    if(len(set(list(res.columns)).
           intersection(['title', 'link', 'updated'])) != 3):
        raise ValueError('Missing Field')

res.to_csv("test.csv")

res = filter_limno(res)
toots = res['title'] + ". " + res['link']

for toot in toots:
    print(toot)
