import pytest
import requests
from selenium.webdriver.common.by import By
from . import DEV_URL
from . import pages


url_exceptions = ["https://twitter.com", "https://www.nature.com"]


@pytest.mark.parametrize("page", pages())
def test_bad_links(setup_chrome, page):
    driver = setup_chrome
    driver.get(DEV_URL + page)
    links = driver.find_elements(By.TAG_NAME, "a")
    warning_links = []
    bad_links = []
    for link in links:
        url = link.get_attribute("href")
        try:
            response_code = int(requests.head(url, timeout=10).status_code)
            if response_code >= 200 and response_code < 300:
                assert True
            elif response_code == 999:
                warning_links.append(f"Warning: {url} returned 999")
                assert True
            else:
                if any(url_exceptions in url):
                    warning_links.append(
                        f"Warning: {url} returned {response_code} but that's expected for bots"
                    )
                else:
                    bad_links.append(f"Bad link {response_code}: {url}")
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidSchema,
            requests.exceptions.MissingSchema,
        ) as e:
            warning_links.append(f"Warning: {url} failed with {e}")

    if warning_links:
        print("\n".join(warning_links))
    if bad_links:
        print("\n".join(bad_links))
        assert False
