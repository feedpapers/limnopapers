import pandas as pd

toot = "Effects of Bark Beetle Disturbance on Soil Nutrient Retention and Lake Chemistry in Glacial Catchment. Ecosystems. http://link.springer.com/10.1007/s10021-018-0298-1"

log = pd.read_csv("log.csv")

keys = ["title", "dc_source", "prism_url"]
title, dc_source, prism_url = toot.split(". ")

d = dict(zip(keys, [title, dc_source, prism_url]))

log.append(pd.DataFrame(data = d))


            title, dc_source, prism_url = toot.split(".")
            d = dict(zip(keys, [list(title),
                                list(dc_source),
                                list(prism_url)]))
            log = log.append(pd.DataFrame(data = d))
            log.to_csv("log.csv")