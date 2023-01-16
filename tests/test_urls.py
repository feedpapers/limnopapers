# https://stackoverflow.com/a/15743618/3362993
import requests
import pkg_resources
import pandas as pd


def url_ok(url):
    # https://stackoverflow.com/a/43167631/3362993
    # url = "https://journals.plos.org/water/feed/atom"
    # url_ok(url)
    headers = requests.utils.default_headers()
    headers["User-Agent"] = (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0)"
        " Gecko/20100101"
        " Firefox/90.0"
    )
    try:
        r = requests.head(url, headers=headers, timeout=10)

        # https://stackoverflow.com/a/39108261/3362993
        if r.status_code == 302:
            jar = r.cookies
            redirect_URL2 = r.headers["Location"]
            r = requests.get(redirect_URL2, cookies=jar)

        return r.status_code in [200, 301, 403]
        response = requests.get(someurl)
    except:
        print(url)
        print(r.status_code)
        return False


def test_urls():
    rawrss = pd.read_csv(pkg_resources.resource_filename("limnopapers", "journals.csv"))
    url_statuses = []
    for i in range(len(rawrss.index)):
        url_statuses.append(url_ok(rawrss["rawrss"][i]))

    print(rawrss[[not i for i in url_statuses]]["rawrss"])
    assert all(url_statuses) is True
