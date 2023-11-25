import requests
from selenium.webdriver.common.by import By
from . import DEV_URL


def test_broken_links(setup_chrome):
    driver = setup_chrome
    driver.get(DEV_URL)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.href
        try:
            response_code = int(requests.head(url).status_code)
            if response_code >= 200 and response_code < 300:
                assert True
            else:
                assert False, f"Bad link: {url}"
        except requests.ConnectionError:
            assert False, f"Broken link: {url}"
