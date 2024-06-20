from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.PageObject import Page


class Music(Page):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, f"{url}/music")

        self.authorize_button = self.driver.find_element(
            By.CLASS_NAME, "authorize-button"
        )
