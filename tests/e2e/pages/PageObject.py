from selenium import webdriver


class Page:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        driver.get(url)
        # Define feautures of the page

    # Define actions on the page
