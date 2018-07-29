import pandas as pd
import datetime

d = {'col1': [1, 2], 'col2': [3, datetime.datetime.now()]}
df = pd.DataFrame(data=d)
df.to_csv("test.csv")