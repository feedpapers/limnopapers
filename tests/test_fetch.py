from limnopapers import *

day = '2018-06-26'
day = '2018-04-11'
day = '2018-04-10'
day = '2018-07-27'

# ---- test full limnotoots ----
data = get_papers(day)        
toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']
toots.to_csv("test.csv")

# ---- test limnotoots guts ----
posts = get_posts(day)
res = pd.DataFrame(posts)
# res.to_csv("test.csv")

res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
res['updated'] = pd.to_datetime(res['updated'])
res = res.sort_values(by = ['updated'])
res = filter_limno(res)
res = filter_today(res, day)
res.to_csv("test.csv")

