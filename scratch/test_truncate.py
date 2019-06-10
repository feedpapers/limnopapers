import pandas as pd

s = pd.Series([
    "Linking landscape heterogeneity with lake dissolved organic"
    "matter properties assessed through absorbance and fluorescence"
    "spectroscopy: Spatial and seasonal patterns in temperate lakes of"
    "Southern Andes (Patagonia, Argentina)", "Testing a short title."])

s[s.str.len() > 159] = s[s.str.len() > 159].str.slice(0, 159) + "..."
s.str.len()
s[0]
