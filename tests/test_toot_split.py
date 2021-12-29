import limnopapers.limnopapers as lp
import limnopapers.utils as utils


def test_toot_split():
    res = lp.toot_split(
        "Zero or not? Causes and consequences of zero‐flow stream gage readings in lakes. test. https://onlinelibrary.wiley.com/doi/abs/10.1002/wat2.1436?af=R"
    )

    assert len(res[0]) > 11  # handling middle q mark

    res = lp.toot_split(
        "Zero or not? test. https://onlinelibrary.wiley.com/doi/abs/10.1002/wat2.1436?af=R"
    )

    assert utils.has_q_mark(res[0])

    res = lp.toot_split(
        "Zero or not. test. https://onlinelibrary.wiley.com/doi/abs/10.1002/wat2.1436?af=R"
    )

    assert res[0].find(".") == -1  # no logging trailing periods
