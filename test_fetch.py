from limnopapers import *

# ---- test full limnotoots ----

if(len(sys.argv) == 2):
    # yyyy-mm-dd format
    data = get_papers(day = sys.argv[1])        
else:
    data = get_papers()        

toots = data['title'] + ". " + data['dc_source']  + ". " + data['prism_url']
for toot in toots:
    print(toot)    

# ---- test limnotoots guts ----
# posts = get_posts(day)
# res = pd.DataFrame(posts)
# res.to_csv("test.csv")

# res.columns = ['title', 'summary', 'prism_url', 'dc_source', 'updated']
# res['updated'] = pd.to_datetime(res['updated'])
# res = res.sort_values(by = ['updated'])
# res = filter_limno(res)
# res = filter_today(res, day)
# res.to_csv("test.csv")

