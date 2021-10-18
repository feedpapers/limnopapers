import importlib.util
import pandas as pd

from limnopapers.limnopapers import toot_construct

spec = importlib.util.spec_from_file_location(
    "limnopapers", "limnopapers/limnopapers.py"
)
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)


def test_toot_construct():

    # --- w missing ending title punctuation, and early question mark
    d = {
        "title": [
            "Contending with Water Shortages in the Pacific? Performance of Private Rainwater Tanks"
        ],
        "dc_source": ["Water Resources Research"],
        "prism_url": [
            "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021WR030350?af=R"
        ],
    }

    res = limnopapers.toot_construct(
        d["title"][0], d["dc_source"][0], d["prism_url"][0]
    )

    assert str(res.__class__) == "<class 'str'>"

    # --- regular

    d = {
        "title": [
            "Contending with Water Shortages in the Pacific: Performance of Private Rainwater Tanks?"
        ],
        "dc_source": ["Water Resources Research"],
        "prism_url": [
            "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021WR030350?af=R"
        ],
    }

    res = limnopapers.toot_construct(
        d["title"][0], d["dc_source"][0], d["prism_url"][0]
    )

    assert str(res.__class__) == "<class 'str'>"


# dt["title"] + ". " + dt["dc_source"] + ". " + dt["prism_url"]

# toots = pd.DataFrame(
#     [
#         [
#             toot_construct(title, dc_source, prism_url)
#             for title, dc_source, prism_url in zip(
#                 data["title"], data["dc_source"], data["prism_url"]
#             )
#         ]
#     ]
# )
