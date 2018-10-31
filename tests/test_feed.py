import os
import sys
import inspect
import feedparser
import pandas as pd

import importlib.util
spec = importlib.util.spec_from_file_location("limnopapers",
                                              "../limnopapers/limnopapers.py")
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)

url = "http://www.publish.csiro.au/RSS_Feed/CSIRO_Publishing_Recent_MF.xml"
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
