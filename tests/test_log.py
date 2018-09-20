import pandas as pd

toot = "Multidecadal climate‐induced changes in Arctic tundra lake geochemistry and geomorphology. Limnology and Oceanography. https://aslopubs.onlinelibrary.wiley.com/doi/abs/10.1002/lno.11015?af=R"

log = pd.read_csv("log.csv")

keys = ["title", "dc_source", "prism_url"]
title, dc_source, prism_url = toot.split(". ")

d = dict(zip(keys, [title, dc_source, prism_url]))
d = pd.DataFrame.from_records(d, index = [0])

log.append(pd.DataFrame(data = d), ignore_index = True)

print(log)