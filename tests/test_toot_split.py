import importlib.util

spec = importlib.util.spec_from_file_location(
    "limnopapers", "limnopapers/limnopapers.py"
)
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)


def test_toot_split():
    test = limnopapers.toot_split(
        "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017. Earth System Science Data. https://doi.org/10.5194/essd-2020-57"
    )
    assert str(test.__class__) == "<class 'list'>"
    assert (
        test[0]
        == "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017"
    )

    # ---

    test = limnopapers.toot_split(
        "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017? Earth System Science Data. https://doi.org/10.5194/essd-2020-57"
    )
    assert str(test.__class__) == "<class 'list'>"
    assert (
        test[0]
        == "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017?"
    )

    # ---

    test = limnopapers.toot_split(
        "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017. Earth System Science Data. https://doi.org/10.5194/essd-2020-57?123"
    )
    assert str(test.__class__) == "<class 'list'>"
    assert (
        test[0]
        == "Annual 30-meter Dataset for Glacial Lakes in High Mountain Asia from 2008 to 2017"
    )
