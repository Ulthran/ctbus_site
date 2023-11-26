import pytest
from . import DEV_URL


@pytest.mark.parametrize(
    "arg",
    [
        "setup_chrome",
        "setup_chrome_mobile",
        "setup_chromium",
        "setup_edge",
        "setup_firefox",
    ],
    indirect=True,
)
def test_title(arg):
    driver = arg
    driver.get(DEV_URL)
    assert driver.title == "Charlie Bushman"
