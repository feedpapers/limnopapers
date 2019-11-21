# https://stmorse.github.io/journal/tidyverse-style-pandas.html

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import wordcloud
import twitter
import config

pd.plotting.register_matplotlib_converters()
pd.set_option('display.expand_frame_repr', False)
sns.set_style('white')

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key = config.access_token_key,
                  access_token_secret=config.access_token_secret)

# prep data
# remove blank dates, remove posted is i
log_raw = pd.read_csv("log.csv")

log = (log_raw
       .dropna(subset = ["date"])
       .loc[log_raw["posted"] == "y"])
log["date"] = pd.to_datetime(log["date"])

# cumulative tweets timeline
# group by date, sum per date, cumulative sum
log_cumsum = (log
              .groupby(["date"])
              .agg(["count"])
              .loc[:, ["date", "title"]]
              .cumsum())

chart = (log_cumsum
         .pipe((sns.lineplot, "data"))
         .legend_.remove())
plt.show()

# per day stats
# calculate day of the week from date, group per day and sum
log['day_of_week'] = log['date'].dt.day_name()
log_perday = (log
              .groupby(["day_of_week"])
              .agg(["count"])
              .loc[:, ["title"]])

# per journal stats
# group per journal and sum
log_perjournal = (log
                  .groupby(["dc_source"])
                  .agg(["count"])
                  .reset_index()
                  .iloc[:, 0:2])
log_perjournal.columns = ["dc_source", "count"]
log_perjournal = log_perjournal.sort_values(by = ["count"], ascending = False)

# title wordcloud
# https://github.com/amueller/word_cloud
wc = wordcloud.WordCloud().generate(log["title"].str.cat(sep=" "))
plt.imshow(wc)
plt.show()

# most favorited
# statuses = api.GetUserTimeline(screen_name="limno_papers", count=200)
# max_id = statuses[199].id
# statuses_2 = api.GetUserTimeline(screen_name="limno_papers", max_id = max_id, count = 200)
# max_id = statuses_2[199].id
# statuses_3 = api.GetUserTimeline(screen_name="limno_papers", max_id = max_id, count = 200)
# with open('tweet_cache_2019', 'wb') as fp:
#    pickle.dump(statuses + statuses_2 + statuses_3, fp)

with open ('tweet_cache_2019', 'rb') as fp:
    statuses = pickle.load(fp)

fav_count = [s.favorite_count for s in statuses]
ids = [s.id for s in statuses]
d = dict(zip(['fav_count', "id"], [fav_count, ids]))
d = (pd.DataFrame.from_records(d)
     .sort_values(by = ["fav_count"], ascending = False))

d[0:3]
