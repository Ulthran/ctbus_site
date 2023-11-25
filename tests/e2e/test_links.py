from selenium.webdriver.common.by import By
from . import DEV_URL


def test_broken_links(setup_chrome):
    driver = setup_chrome
    driver.get(DEV_URL)
    links = driver.find_element(By.TAG_NAME, "a")
    print(str(links))
    for link in links:
        print(str(link))
        url = link.get_attribute("href")
        if url:
            if url.startswith(DEV_URL):
                driver.get(url)
                assert driver.title != "404 Not Found"
            else:
                assert url.startswith("http")
                driver.get(url)
                assert driver.title != "404 Not Found"
