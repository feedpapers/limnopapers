import os
import pandas as pd

import limnopapers.utils as utils
import limnopapers.limnopapers as lp

# read test data from json
test_data = utils.load_dict_from_file("tests/test_data.json")

# ----

# pass to get_posts_
posts = []
posts_raw = lp.get_posts_("test", feed_dict=test_data)
posts.append(posts_raw)

os.remove("tests/test_log.csv")

data = lp.get_papers(posts=posts, log_path="tests/test_log.csv")

lp.limnotoots(
    tweet=False,
    interactive=True,
    data=data,
    log_path="tests/test_log.csv",
    ignore_all=True,
)

log = pd.read_csv("tests/test_log.csv").iloc[-1:, :]

log
