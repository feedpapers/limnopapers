# https://stackoverflow.com/a/42145604/3362993


def pytest_addoption(parser):
    parser.addoption("--ignore_cache", action="store_true", default=False)


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.ignore_cache
    if "ignore_cache" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("ignore_cache", [option_value])
