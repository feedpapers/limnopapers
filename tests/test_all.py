import pandas as pd
import pytest

import importlib.util
spec = importlib.util.spec_from_file_location("limnopapers",
                                              "limnopapers/limnopapers.py")
limnopapers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(limnopapers)


def test_running():
    limnopapers.limnotoots(tweet = False, interactive = False, to_csv = True)
    d = pd.read_csv("test.csv")
    assert isinstance(d, pd.DataFrame)
