import re
from playwright.sync_api import Page
from pages_playwright.basic_page import BasicPage


class SearchPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"first_book_found": 'xpath=//*[@id="root"]/div/div/div/div[1]/div/div[1]'}

    def found(self, book_name):
        return book_name in self._page.locator(*self._locators["first_book_found"]).inner_text
