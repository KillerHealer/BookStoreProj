from selenium import webdriver
from selenium.webdriver.common.by import By
from BasicPage import BasicPage


class LoginPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._locators = {"email_locate": (By.ID, "email"),
                          "login_form": (By.ID, "login_form"),
                          "password_locate": (By.ID, "passwd"),
                          "login_btn_locate": (By.ID, "SubmitLogin"),
                          "forgot-password": (By.XPATH, '//a[text()="Forgot your password?"]')}

    def login(self, username: str, password: str):
        login_form = self._driver.find_element(*self._locators["login_form"])
        login_form.find_element(*self._locators["email_locate"]).send_keys(username)
        login_form.find_element(*self._locators["password_locate"]).send_keys(password)
        login_form.find_element(*self._locators["login_btn_locate"]).click()
        return self._driver