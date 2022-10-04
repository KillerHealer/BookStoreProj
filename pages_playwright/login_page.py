from playwright.sync_api import Page
from pages_playwright.basic_page import BasicPage


class LoginPage(BasicPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._locators = {"email_locate": (By.ID, "email"),
                          "login_form": (By.ID, ""),
                          "password_locate": (By.ID, "password"),
                          "login_btn_locate": (By.XPATH, '//*[text() = "Submit"]')}

    def login(self, username: str, password: str):
        login_form = self._page
        login_form.locator(*self._locators["email_locate"]).type(username)
        login_form.locator(*self._locators["password_locate"]).type(password)
        login_form.locator(*self._locators["login_btn_locate"]).click()
        return self._page
