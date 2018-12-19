import os
import sys
import inspect
import pdb
import feedparser
import pandas as pd
import datetime
import twitter
from colorama import Fore
import argparse

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

try:
    import config
except:
    print("No twitter keys found")


def filter_limno(df):

    df = df.reset_index()

    filter_for = ["lake", "reservoir", "inland waters", "stream water",
                  "water quality"]
    has_limno_title = df['title'].str.contains('|'.join(filter_for),
                                               case = False)
    has_limno_summary = df['summary'].str.contains('|'.join(filter_for),
                                                   case = False)

    is_limno = pd.DataFrame([has_limno_title, has_limno_summary]) \
        .transpose() \
        .sum(axis = 1) > 0

    df = df[is_limno]

    filter_against = ['ocean', 'iran', 'fault', 'wetland',
                      'hydroelectric', ' mining ', 'Great Lakes', '^sea$',
                      'hydropower', '^ Part ', 'woolly', 'Lake Erie',
                      'Lake Michigan', 'russia', 'spawning', 'salmon', 'trout',
                      'walleye', 'coastal', 'fish diet', 'arctic char',
                      'estuaries', 'hydroxide', 'fluid injection',
                      'cover image', 'economic value', 'google earth',
                      'alewife', 'largemouth bass', 'fish metapopulations',
                      'antibiotic', 'acetaminophen', 'viruses', 'evolutionary',
                      'china', 'italy', 'unmanned aerial', 'cohort',
                      'capillary tubes', 'water security', 'spillway',
                      'near .{1,17} Lake', 'environmental DNA', 'indonesia',
                      'water utility', 'phages', 'microbiome',
                      'water distribution systems', 'raindrop',
                      'emerging technologies', 'microbial abundance',
                      'video mapping', 'community garden',
                      'student monitoring', 'hydrograph separation',
                      'slovenia', 'mongolia', 'individual stones',
                      'drinking water', 'correction to\:', 'polymerase',
                      'mud carp', 'groundwater status', 'water system planner',
                      'agribusiness', 'amplicon', 'gene expression',
                      '16S rRNA', 'Enterococcus', 'lead service line',
                      'nesting', 'hatching',
                      'environmental literacy', 'adenosine', 'lithology',
                      'nanotubes', 'magnetic']
    has_junk_summary = ~df['summary'].str.contains('|'.join(filter_against),
                                                   case = False)
    has_junk_title = ~df['title'].str.contains('|'.join(filter_against),
                                               case = False)

    not_junk = pd.DataFrame([has_junk_summary, has_junk_title]) \
        .transpose() \
        .sum(axis = 1) == 2

    return(df[not_junk])


def filter_today(df, day):
    today_parsed = datetime.datetime.strptime(
        day + " 09:00:00", "%Y-%m-%d %H:%M:%S")
    yesterday = today_parsed - datetime.timedelta(days = 1)
    tomorrow = today_parsed + datetime.timedelta(days = 0)
    published_today = (df['updated'] > yesterday) & (df['updated'] < tomorrow)
    res_today = df[published_today]
    return(res_today)


def get_posts_(title, url):
    # print(url)
    feed = feedparser.parse(url)
    posts = []
    for post in feed.entries:
        try:
            posts.append((post.title, post.summary, post.link,
                          title, post.updated))
        except AttributeError:
            try:
                posts.append((post.title, post.summary, post.link,
                              title, post.published))
            except AttributeError:
                try:
                    posts.append((post.title, post.summary, post.link,
                                  title, None))
                except AttributeError:
                    try:
                        posts.append((None, None, None, None, None))
                    except AttributeError:
                        pass

    res = pd.DataFrame(posts)
    # print(res.columns)
    try:
        res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
    except AttributeError:
        pass
    return(res)


def get_posts():
    # https://stackoverflow.com/questions/45701053/get-feeds-from-feedparser-and-import-to-pandas-dataframe
    rawrss = pd.read_csv("journals.csv")

    # sort rawrss by increasing journal name nchar length for pretty printing
    rawrss.index = rawrss['title'].str.len()
    rawrss = rawrss.sort_index().reset_index(drop = True)

    posts = []
    for i in range(len(rawrss.index)):
        sys.stdout.write('\b' * 1000)
        sys.stdout.write('Fetching papers from: ' + rawrss['title'][i] + '\r')

        try:
            single_posts = get_posts_(rawrss['title'][i], rawrss['rawrss'][i])
            posts.append(single_posts)
        except AttributeError:
            pass

    print('\n')
    return(posts)


def get_papers(to_csv = False):
    posts = get_posts()
    res = pd.concat(posts)
    res['updated'] = pd.to_datetime(res['updated'])
    res = res.sort_values(by = ['updated'])
    res = res.drop_duplicates(subset = ['title'], keep = 'first')
    # rm entries that are also in log
    log = pd.read_csv("log.csv")
    res = res[~res['title'].isin(log['title'])]

    res_limno = filter_limno(res)

    if to_csv is not False:
        res_limno.to_csv("test_limno.csv")
        res.to_csv("test.csv")

    dfs = {}
    dfs['res'] = res
    dfs['res_limno'] = res_limno

    return(dfs)


def limnotoots(tweet, interactive, to_csv = False):
    data = get_papers(to_csv)
    filtered = data["res_limno"]
    data = filter_today(data["res"], day = str(datetime.date.today()))

    if(len(data.index) != 0 or len(filtered.index) != 0):
        print(Fore.RED + "Excluded: ")
        print()
        toots = data['title'] + ". " + data['dc_source'] + ". " + \
            data['prism_url']
        for toot in toots:
            print(Fore.RED + toot)
            print()

        print(Fore.GREEN + "Filtered: ")
        print()
        toots = filtered['title'] + ". " + filtered['dc_source'] + ". " + \
            filtered['prism_url']
        for toot in toots:
            print(Fore.GREEN + toot)
            print()

        if(tweet is True):
            api = twitter.Api(consumer_key=config.consumer_key,
                              consumer_secret=config.consumer_secret,
                              access_token_key = config.access_token_key,
                              access_token_secret=config.access_token_secret)
            # print(api.VerifyCredentials())

            # toots = filtered['title'] + ". " + filtered['dc_source'] + ". " \
            # + filtered['prism_url'] + filtered['updated']
            for toot in toots:
                print(toot)
                if(interactive is True):
                    post_toot = input("post limnotoot (y)/n/i? ") or "y"
                    if(post_toot in ["y"]):
                        status = api.PostUpdate(toot)
                        posted = "y"
                    if(post_toot in ["i"]):
                        posted = "i"

                    # write to log
                    log = pd.read_csv("log.csv")
                    keys = ["title", "dc_source", "prism_url", "posted",
                            "date"]

                    title, dc_source, prism_url = toot.split(". ")
                    date = str(datetime.date.today())
                    d = dict(zip(keys, [title, dc_source, prism_url,
                                        posted, date]))
                    d = pd.DataFrame.from_records(d, index=[0])
                    log = log.append(pd.DataFrame(data = d),
                                     ignore_index = True)
                    log.to_csv("log.csv", index = False)
                else:
                    status = api.PostUpdate(toot)

                    # write to log
                    log = pd.read_csv("log.csv")
                    keys = ["title", "dc_source", "prism_url"]
                    title, dc_source, prism_url = toot.split(". ")
                    d = dict(zip(keys, [title, dc_source, prism_url]))
                    d = pd.DataFrame.from_records(d, index=[0])
                    log = log.append(pd.DataFrame(data = d))
                    log.to_csv("log.csv", index = False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tweet', default = False,
                        action='store_true')
    parser.add_argument('--interactive', default = False,
                        action='store_true')
    args = parser.parse_args()

    limnotoots(tweet = args.tweet, interactive = args.interactive)

if __name__ == "__main__":
    main()
