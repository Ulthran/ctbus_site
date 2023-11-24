import pytest
from . import DEV_URL


@pytest.mark.parametrize("setup", [(setup_chrome)])
def test_title(setup):
    driver = setup
    driver.get(DEV_URL)
    assert driver.title == "Charlie Bushman"


@pytest.mark.parametrize("setup", [(setup_chrome)])
def test_title_certs(setup):
    driver = setup
    driver.get(f"{DEV_URL}/certifications")
    print(driver.title)
