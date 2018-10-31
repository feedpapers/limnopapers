import pandas as pd

df1 = pd.DataFrame(data = {'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame(data = {'col1': [1, 2], 'col2': [6, 5]})

dfs = {}
dfs['df1'] = df1
dfs['df2'] = df2

print(dfs['df2'])
