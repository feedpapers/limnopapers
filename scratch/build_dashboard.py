import pandas as pd
import datetime
from limnopapers import limnotoots


# get latest tweet date per dc_source
log_raw = pd.read_csv("log.csv")
log_raw['date'] = pd.to_datetime(log_raw['date'])
labels = log_raw.groupby('dc_source').date.idxmax()
log = log_raw.loc[log_raw.index.intersection(labels)]
log = log.reset_index(drop = True)
log.loc[log['posted'] != "i"]

# get number of tweets per dc_source
# log_raw.groupby('dc_source').size()

# get latest rss posting per dc_source
# execute a dry run to csv without limno filtering
limnotoots(tweet = False, interactive = False, to_csv = True)
d = pd.read_csv("test.csv")
d['updated'] = pd.to_datetime(d['updated'])
labels = d.groupby('dc_source').updated.idxmax()
d = d.loc[d.index.intersection(labels)]
d = d.reset_index(drop = True)

# create tables
