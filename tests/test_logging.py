import os
import pandas as pd

import limnopapers.utils as utils
import limnopapers.limnopapers as lp


def test_logging():

    # read test data from json
    test_data_raw = utils.load_dict_from_file("tests/test_data.json")

    # ---- ensure logging handles middle q marks ----
    test_data = test_data_raw.copy()
    test_data["entries"] = [test_data["entries"][0]]

    posts = []
    posts_raw = lp.get_posts_("test", feed_dict=test_data)
    posts.append(posts_raw)

    if os.path.exists("tests/test_log.csv"):
        os.remove("tests/test_log.csv")

    data = lp.get_papers(posts=posts, log_path="tests/test_log.csv")

    tooted = lp.limnotoots(
        tweet=False,
        interactive=True,
        data=data,
        log_path="tests/test_log.csv",
        ignore_all=True,
    )

    log = pd.read_csv("tests/test_log.csv").iloc[1:, :].reset_index(drop=True)

    assert utils.has_q_mark(log["title"][0])

    # ---- ensure no toots in log are re-tooted ----
    test_data = test_data_raw.copy()

    posts = []
    posts_raw = lp.get_posts_("test", feed_dict=test_data)
    posts.append(posts_raw)

    if os.path.exists("tests/test_log.csv"):
        os.remove("tests/test_log.csv")

    data = lp.get_papers(posts=posts, log_path="tests/test_log.csv")
    tooted = lp.limnotoots(
        tweet=False,
        interactive=True,
        data=data,
        log_path="tests/test_log.csv",
        ignore_all=True,
    )
    # pd.read_csv("tests/test_log.csv").iloc[1:, :].reset_index(drop=True)
    assert len(tooted) == 4

    data = lp.get_papers(posts=posts, log_path="tests/test_log.csv")
    tooted = lp.limnotoots(
        tweet=False,
        interactive=True,
        data=data,
        log_path="tests/test_log.csv",
        ignore_all=True,
    )

    assert len(tooted) == 0
