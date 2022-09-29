import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
from pages_selenium.home_page import HomePage
from pages_selenium.login_page import LoginPage
from pages_selenium.search_page import SearchPage


@pytest.fixture()
def home_page():
    """
    gets page to login page
    :return:
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrom_driver_path = "D:\Pyprojects\chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("http://localhost/store")
    home_page = HomePage(driver)
    return home_page


def test_login(home_page):
    """
    goes from the home page to login page and tries to log in with normal credentials
    :param home_page:
    :return:
    """
    time.sleep(1)
    login_page = LoginPage(home_page.signIn())
    home_page = HomePage(login_page.login("noam@example.com", "string"))
    time.sleep(1)
    home_page.logOut()
    assert home_page.loggedOut()
    home_page.close()


def test_buy(home_page):
    """
    logs in and tries to buy a book with the name provided
     if the stock is 0 it buys Animal Farm
    :param home_page:
    :return:
    """
    time.sleep(1)
    login_page = LoginPage(home_page.signIn())
    home_page = HomePage(login_page.login("noam@example.com", "string"))
    time.sleep(1)
    assert home_page.buyBook(home_page.searchBook("The Hunger Games"))
    home_page.close()


def test_search(home_page):
    """
    Search the term in the search bar and check it was found
    :param home_page:
    :return:
    """
    search_page = SearchPage(home_page.search("Catching"))
    assert search_page.found("Catching Fire")
    search_page.close()
