import pandas as pd

toot = "Assessment of methane and carbon dioxide emissions in two sub‐basins of a small acidic bog lake artificially divided 30 years ago. Freshwater Biology. https://onlinelibrary.wiley.com/doi/abs/10.1111/fwb.13182?af=R"

log = pd.read_csv("log.csv")

keys = ["title", "dc_source", "prism_url"]
title, dc_source, prism_url = toot.split(". ")

d = dict(zip(keys, [list(title), list(dc_source), list(prism_url)]))

log.append(pd.DataFrame(data = d))


            title, dc_source, prism_url = toot.split(".")
            d = dict(zip(keys, [list(title),
                                list(dc_source),
                                list(prism_url)]))
            log = log.append(pd.DataFrame(data = d))
            log.to_csv("log.csv")