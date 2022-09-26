from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_selenium.basic_page import BasicPage


class HomePage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Sign-In": (By.XPATH, '//*[@id="root"]/nav/div/div/a[3]'),
                          "search-box": (By.ID, ""),
                          "logout": (By.XPATH, '//*[text() = "Log Out"]'),
                          "search-btn": (By.NAME, "")}

    def signIn(self):
        self._driver.find_element(*self._locators["Sign-In"]).click()
        return self._driver

    def logOut(self):
        self._driver.find_element(*self._locators["logout"]).click()
        return self._driver

    def loggedOut(self):
        return len(self._driver.find_elements(*self._locators["logout"])) == 0

    def search(self, search_word):
        self._driver.find_element(*self._locators["search-box"]).send_keys(search_word)
        self._driver.find_element(*self._locators["search-btn"]).click()
        return self._driver
