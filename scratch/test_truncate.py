import pandas as pd

d = {'title': ["Linking landscape heterogeneity with lake dissolved organic"
               "matter properties assessed through absorbance and fluorescence"
               "spectroscopy: Spatial and seasonal patterns in temperate lakes of"
               "Southern Andes (Patagonia, Argentina)", "Testing a short title."],
     'col2': [3, 4]}
df = pd.DataFrame(data=d)

# good
titles = df['title'].copy()
titles[titles.str.len() > 159] = titles[titles.str.len() > 159].str.slice(0, 159) + "..."
titles.str.len()
titles[0]

# bad
titles = df['title']
titles[titles.str.len() > 159] = titles[titles.str.len() > 159].str.slice(0, 159) + "..."
titles.str.len()
titles[0]