s = "a.b.c"

keys = ["title", "dc_source", "prism_url"]
title, dc_source, prism_url = s.split(".")

d = dict(zip(keys, [list(title), list(dc_source), list(prism_url)]))

pd.DataFrame(data = d)
