import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_selenium.basic_page import BasicPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"Sign-In": (By.XPATH, '//*[@id="root"]/nav/div/div/a[3]'),
                          "search-box": (By.ID, "searchtext"),
                          "logout": (By.XPATH, '//*[text() = "Log Out"]'),
                          "card-body": (By.CLASS_NAME, "card-body"),
                          "card-footer": (By.CLASS_NAME, "card-footer"),
                          "buy-book-btn": (By.CLASS_NAME, "card-footer"),
                          "search-btn": (By.XPATH, '//*[@id="root"]/nav/div/form/button')}

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
        time.sleep(1)
        self._driver.find_element(*self._locators["search-btn"]).click()
        time.sleep(1)
        self._driver.find_element(*self._locators["search-btn"]).click()
        return self._driver

    def searchBook(self, bookName: str):
        """
        searches for a book in the list with the name provided
        :param bookName:
        :return:
        """
        bookList = self._driver.find_elements(By.CLASS_NAME, "book-container")
        for card in bookList:
            s = card.find_element(*self._locators["card-body"]).text
            if bookName in s:
                if "Left In Stock: 0" in card.text:
                    break
                return card
        return bookList[0]

    def buyBook(self, book_card):
        """
        buys the book received by the card
        :param book_card:
        :return:
        """
        footer = book_card.find_element(*self._locators["card-footer"])
        stock = [int(num) for num in re.findall(r"\d+", footer.text.split()[5])][0]
        title = book_card.text.partition('\n')[0]
        footer.find_element(*self._locators["buy-book-btn"]).click()
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.ENTER)
        try:
            actions.perform()
        except Exception:
            pass
        self._driver.refresh()
        time.sleep(1)
        book_card = self.searchBook(title)
        stock2 = [int(num) for num in re.findall(r"\d+", book_card.find_element(By.CLASS_NAME, "card-footer").text.split()[5])][0]
        if stock - 1 == stock2:
            return True
        else:
            return False



