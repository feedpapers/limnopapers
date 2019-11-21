# https://stmorse.github.io/journal/tidyverse-style-pandas.html

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters()
pd.set_option('display.expand_frame_repr', False)
sns.set_style('white')

log_raw = pd.read_csv("log.csv")

# prep data
# remove blank dates, remove posted is i
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

# most favorited
