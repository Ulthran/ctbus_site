from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.PageObject import Page


class Comps(Page):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, url)

        self.hide_graphs_button = self.driver.find_element(
            By.CLASS_NAME, "interest-button"
        )
        self.lorenz_plots = self.driver.find_element(By.ID, "LorenzPlots")
