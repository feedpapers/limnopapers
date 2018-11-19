import os
import sys
import inspect
import feedparser
import pandas as pd
import pytest

import importlib.util
spec = importlib.util.spec_from_file_location("limnopapers",
                                              "limnopapers/limnopapers.py")
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)

url = "http://rss.sciencedirect.com/publication/science/03043800"
posts = []

feed = feedparser.parse(url)
for post in feed.entries:
    posts.append(post)

res = pd.DataFrame(posts)


def test_fields():
    has_published = len(set(list(res.columns)).
                        intersection(['title', 'link', 'published'])) == 3
    has_updated = len(set(list(res.columns)).
                      intersection(['title', 'link', 'updated'])) == 3
    assert has_published or has_updated

res.to_csv("test.csv")

res = limnopapers.filter_limno(res)
toots = res['title'] + ". " + res['link']

for toot in toots:
    print(toot)
