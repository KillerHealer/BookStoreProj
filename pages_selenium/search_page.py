import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_selenium.basic_page import BasicPage


class SearchPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"first_book_found": (By.CLASS_NAME, "card-body")}

    def found(self, book_name):
        return book_name in self._driver.find_element(*self._locators["first_book_found"]).text



