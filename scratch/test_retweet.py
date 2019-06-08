import twitter
import pandas as pd
import limnopapers as lp
try:
    import config
except:
    print("No twitter keys found")


api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key = config.access_token_key,
                  access_token_secret=config.access_token_secret)

user = "JEnvironQual"
statuses = api.GetUserTimeline(screen_name = user)

res = []
for p in statuses:
    res.append({'title': p.text, 'summary': p.text, 'id': p.id})
res = pd.DataFrame(res)

res_limno = lp.filter_limno(res)
[statuses[i] for i in res_limno['papers']['index']]

# retweet
api.PostRetweet()
