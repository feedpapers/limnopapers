import os
import sys
import inspect
import feedparser as fp
import pandas as pd
import pytest

import importlib.util
spec = importlib.util.spec_from_file_location("limnopapers",
                                              "limnopapers/limnopapers.py")
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)

url = "https://www.tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=tinw20"
posts = []

feed = fp.parse(url)
for post in feed.entries:
    posts.append(post)

res = pd.DataFrame(posts)
# res = res.rename(columns = {"link": "prism_url"})
# print(res.columns)
res.filter(items = ["updated"])


def test_fields():
    has_published = len(set(list(res.columns)).
                        intersection(['title', 'link'])) == 2
    has_updated = len(set(list(res.columns)).
                      intersection(['title', 'link'])) == 2
    assert has_published or has_updated

res.to_csv("test.csv")

print(res)
res = limnopapers.filter_limno(res)['papers']
print(res)
print(res['title'])
toots = res['title'] + ". " + res['link']

for toot in toots:
    print(toot)
