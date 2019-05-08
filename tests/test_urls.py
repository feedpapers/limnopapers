# https://stackoverflow.com/a/15743618/3362993
import requests
import pkg_resources
import pandas as pd
import pytest
from socket import error as SocketError
import errno


def url_ok(url):
    # https://stackoverflow.com/a/43167631/3362993
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    try:
        r = requests.head(url, headers = headers)
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
