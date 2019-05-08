# https://stackoverflow.com/a/15743618/3362993
import requests


def url_ok(url):
    try:
        r = requests.head(url)
        return r.status_code in [200, 301]
    except:
        return False

url_ok("http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1939-5590")
url_ok("https://notaurljki.com")
