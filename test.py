from limnopapers import *

day = '2018-06-26'
day = '2018-04-11'
day = '2018-04-10'

posts = get_posts(day)
res = pd.DataFrame(posts)
res.to_csv("test.csv")

res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
res['updated'] = pd.to_datetime(res['updated'])
res = res.sort_values(by = ['updated'])
res = filter_limno(res)
res.to_csv("test.csv")
res = filter_today(res, day)

get_papers(day)


