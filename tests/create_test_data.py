import limnopapers.utils as utils


posts = [
    (
        "Zero or not? Causes and consequences of zero‐flow stream gage readings in lakes",
        "test",
        "https://onlinelibrary.wiley.com/doi/abs/10.1002/wat2.1436?af=R",
        "WIREs Water",
        "2021-12-27T12:30:54-08:00",
    ),
    (
        "Multidecadal climate‐induced changes in Arctic tundra lake geochemistry and geomorphology",
        "test",
        "https://aslopubs.onlinelibrary.wiley.com/doi/abs/10.1002/lno.11015?af=R",
        "Limnology and Oceanography",
        "2021-12-27T12:30:54-08:00",
    ),
    (
        "Annual 30-meter Dataset for Glacial Lakes in High Mountain from 2008 to 2017?",
        "test",
        "https://doi.org/10.5194/essd-2020-57",
        "Earth System Science Data",
        "2021-12-27T12:30:54-08:00",
    ),
    (
        "Horizontal migration of zooplankton in lake-wetland interfaces. Can temperature-driven surface exchange flows modulate its patterns?",
        "test",
        "http://link.springer.com/10.1007/s00027-024-01046-1",
        "Aquatic Sciences",
        "2021-12-27T12:30:54-08-00",
    ),
    (
        "This is a paper about nothing.",
        "test",
        "http://link.springer.com/10.1007/s00027-024-01046-1",
        "Nothing",
        "2021-12-27T12:30:54-08-00",
    ),
]

keys = ["title", "summary", "prism_url", "dc_source", "updated"]
keys_consolidated = ["title", "summary", "prism_url", "dc_source", "updated"]

# re-create feedparser results structure
posts_zipped = [zip(keys_consolidated, post) for post in posts]
dt = [utils.zip_to_dict(sub_zip, keys) for sub_zip in posts_zipped]

dt_nested = {"entries": dt}

utils.save_dict_to_file(dt_nested, "tests/test_data.json")

# --- exploring feedparser results structure ---

# import limnopapers.limnopapers as lp
# import limnopapers.utils as utils

# test = utils.load_dict_from_file("fixtures/test_get_posts_.json")
# test_posts = test["entries"][1:3]  # test["entries"] is a list of dict objects
# keys = ["title", "summary", "prism_url", "updated"]

# target = [{key: post[key] for key in keys} for post in test_posts]

# posts = []
# for post in test_posts:
#     post_consolidated = lp.consolidate_dict(posts, post, "test")
#     posts = post_consolidated[0]

# keys_consolidated = post_consolidated[1]

# posts_zipped = [zip(keys_consolidated, post) for post in posts]
# rebuilt = [utils.zip_to_dict(sub_zip, keys) for sub_zip in posts_zipped]

# target
# rebuilt

# rebuilt_nested = {"entries": rebuilt}
# lp.get_posts_("test", feed_dict=rebuilt_nested)
# lp.get_posts_("test", feed_dict=test).head(1)
