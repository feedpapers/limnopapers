import pandas as pd
import datetime
from limnopapers import limnotoots
from numpy import nan as Nan


# get latest tweet date per dc_source
log_raw = pd.read_csv("log.csv")
log_raw['date'] = pd.to_datetime(log_raw['date'])
labels = log_raw.groupby('dc_source').date.idxmax()
log = log_raw.loc[log_raw.index.intersection(labels)]
log = log.reset_index(drop = True)
log = log.loc[log['posted'] != "i"]
log['date'] = log['date'].dt.strftime("%Y-%m")

# get number of tweets per dc_source
limnotoots(tweet = False, interactive = False, to_csv = True)
d = pd.read_csv("test.csv")
d['updated'] = pd.to_datetime(d['updated'])
labels = d.groupby('dc_source').updated.idxmax()
d = d.loc[d.index.intersection(labels)]
d = d.reset_index(drop = True)
d['updated'] = d['updated'].dt.strftime("%Y-%m")

# create tables
latest = log.assign(badge = "![alt text](https://img.shields.io/badge/" +
                    log['dc_source'] +
                    "-" + log['date'].replace(regex = "-", value = "--") +
                    "-green.svg)")
latest = latest[['badge']]

state = d.assign(badge = "![alt text](https://img.shields.io/badge/" +
                 d['dc_source'] +
                 "-" + d['updated'].replace(regex = "-", value = "--") +
                 "-green.svg)")
state = state[['badge']]

cols = "| " + latest.columns + " |"
blank_line = pd.Series([Nan], index=cols)
header = pd.DataFrame([['---',] * len(cols)], columns = cols)
table = pd.concat([header, latest])
table = table.append(blank_line, ignore_index=True)
table = table.rename(index=str, columns={"badge": "Last tweet"})
table.to_csv("dashboard.md", sep="|", index=False)

table = open("dashboard.md", "a")
table.write("\n")
table.close()

cols = "| " + state.columns + " |"
blank_line = pd.Series([Nan], index=cols)
header = pd.DataFrame([['---',] * len(cols)], columns=cols)
table = pd.concat([header, state])
table = table.rename(index=str, columns={"badge": "Last RSS entry"})
table.to_csv("dashboard.md", sep="|", mode = "a", index=False)
