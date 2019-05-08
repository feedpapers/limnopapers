# https://stackoverflow.com/a/15743618/3362993
import requests
import pkg_resources
import pandas as pd
import pytest


def url_ok(url):
    #  url = "https://academic.oup.com/rss/site_5266/3132.xml"
    try:
        r = requests.head(url)
        return r.status_code in [200, 301]
    except:
        print(url)
        return False


def test_urls():
    rawrss = pd.read_csv(pkg_resources.resource_filename('limnopapers',
                                                         'journals.csv'))
    url_statuses = []
    for i in range(len(rawrss.index)):
        url_statuses.append(url_ok(rawrss['rawrss'][i]))

    assert all(url_statuses) is True
