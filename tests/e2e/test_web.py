import pytest
from . import DEV_URL


@pytest.mark.parametrize(
    "arg",
    [
        "setup_chrome",
        "setup_chromium",
        "setup_brave",
        "setup_edge",
        "setup_firefox",
        "setup_ie",
    ],
    indirect=True,
)
def test_title(arg):
    driver = arg
    driver.get(DEV_URL)
    assert driver.title == "Charlie Bushman"
