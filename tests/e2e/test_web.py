import pytest
from . import DEV_URL
from tests.e2e.pages import Index, Comps


WEBDRIVERS = [
    "setup_chrome",
    "setup_chrome_mobile",
    "setup_chromium",
    "setup_edge",
    "setup_firefox",
]


@pytest.mark.parametrize("arg", WEBDRIVERS, indirect=True)
def test_index(arg):
    driver = arg
    index = Index(driver, DEV_URL)
    assert index.title == "Charlie Bushman"


@pytest.mark.parametrize("arg", WEBDRIVERS, indirect=True)
def test_comps(arg):
    driver = arg
    driver.get(DEV_URL)

    comps = Comps(driver)
    comps.hide_graphs_button.click()
    assert not comps.lorenz_plots.is_displayed()

    comps.hide_graphs_button.click()
    assert comps.lorenz_plots.is_displayed()
