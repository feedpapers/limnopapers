# pytest -s tests/test_get_posts.py --ignore_cache

import json
import feedparser
import limnopapers.limnopapers as lp

import limnopapers.utils as utils


cache_path = "fixtures/test_get_posts.json"


def test_get_posts_(ignore_cache):
    title = "Limnology and Oceanography"
    url = "https://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1939-5590"

    import os

    if not os.path.exists(cache_path) or ignore_cache:
        feed_dict = feedparser.parse(url)
        utils.save_dict_to_file(feed_dict, cache_path)
    else:
        feed_dict = utils.load_dict_from_file(cache_path)

    lno = lp.get_posts_(title, url, feed_dict)

    assert str(lno.__class__) == "<class 'pandas.core.frame.DataFrame'>"
