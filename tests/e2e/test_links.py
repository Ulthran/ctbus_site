import os
import requests
from selenium.webdriver.common.by import By
from . import DEV_URL
from app.app import app

app.url_map
for template in os.listdir(os.path.join(app.root_path, "templates")):
    print(template)


def test_broken_links(setup_chrome):
    driver = setup_chrome
    driver.get(DEV_URL)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        url = link.get_attribute("href")
        try:
            response_code = int(requests.head(url).status_code)
            if response_code >= 200 and response_code < 300:
                assert True
            elif response_code == 999:
                print(f"Warning: {url} returned 999")
                assert True
            else:
                assert False, f"Bad link: {url}"
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidSchema,
        ) as e:
            print(f"Warning: {url} failed with {e}")
