import time
import re
from playwright.sync_api import Page
from pages_playwright.basic_page import BasicPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"Sign-In": 'text=Log In',
                          "search-box": "text=Books Or Authors",
                          "logout": "text=Log Out",
                          "book-container": 'xpath=//*[@id="root"]/div/div/div/div',
                          "card-body": 'xpath=//*[@id="root"]/div/div/div/div[1]/div/div[1]',
                          "card-footer": 'xpath=//*[@id="root"]/div/div/div/div[2]/div/div[2]',
                          "buy-book-btn": "text=Purchase",
                          "search-btn": "text=Search"}

    def signIn(self):
        self._page.locator(*self._locators["Sign-In"]).click()
        return self._page

    def logOut(self):
        self._page.locator(*self._locators["logout"]).click()
        return self._page

    def loggedOut(self):
        return len(self._page.query_selector_all(*self._locators["logout"])) == 0

    def search(self, search_word):
        self._page.locator(*self._locators["search-box"]).type(search_word)
        time.sleep(1)
        self._page.locator(*self._locators["search-btn"]).click()
        time.sleep(1)
        self._page.locator(*self._locators["search-btn"]).click()
        return self._page

    def searchBook(self, bookName: str):
        """
        searches for a book in the list with the name provided
        :param bookName:
        :return:
        """
        bookList = self._page.query_selector_all(self._locators["book-container"])
        for card in bookList:
            s = card.query_selector(*self._locators["card-body"]).inner_text()
            if bookName in s:
                if "Left In Stock: 0" in card.inner_text:
                    break
                return card
        return bookList[0]

    def buyBook(self, book_card):
        """
        buys the book received by the card
        :param book_card:
        :return:
        """
        footer = book_card.locator(*self._locators["card-footer"])
        stock = [int(num) for num in re.findall(r"\d+", footer.text.split()[5])][0]
        title = book_card.text.partition('\n')[0]
        footer.locator(*self._locators["buy-book-btn"]).click()
        actions = ActionChains(self._page)
        actions.send_keys(Keys.ENTER)
        try:
            actions.perform()
        except Exception:
            pass
        self._page.reload()
        time.sleep(1)
        book_card = self.searchBook(title)
        stock2 = [int(num) for num in re.findall
        (r"\d+", book_card.locator(*self._locators["card-footer"]).text.split()[5])][0]
        if stock - 1 == stock2:
            return True
        else:
            return False
