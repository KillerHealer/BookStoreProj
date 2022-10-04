import logging
import re
import time
import pytest
from playwright.sync_api import Page, expect
from pages_playwright.home_page import HomePage
from pages_playwright.login_page import LoginPage
from pages_playwright.search_page import SearchPage


@pytest.fixture()
def home_page(page: Page):
    """
    gets page to login page
    :return:
    """
    page.goto("http://localhost/store")
    home_page = HomePage(page)
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
