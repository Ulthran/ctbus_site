from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.PageObject import Page


class Index(Page):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)

        self.title = self.driver.title
        self.buttons = self.driver.find_elements(By.CLASS_NAME, "interest-button")
