import pytest
import logging
import requests
from API.account_api import AccountApi
from Models.account import Account
from Models.authResponseDto import AuthResponseDto
from API.book_api import BookApi
from API.author_api import AuthorApi
emailNum = 2
my_account = Account(f"hhh{emailNum}@example.com", "123456", "noam", "barkai")
apiAC = AccountApi()
apiAU = AuthorApi()
apiB = BookApi()


@pytest.mark.account()
def test_post_account_register():
    """
    tries to register a new account to the system
    :return:
    """
    global emailNum, my_account
    logging.info("trying to add a new account")
    assert apiAC.post_register(my_account)
    acc = apiAC.post_login(my_account.email, my_account.password)
    assert isinstance(acc, AuthResponseDto)
    emailNum += 1

@pytest.mark.account()
def test_post_account_refreshtoken():
    acc = apiAC.post_login(my_account.email, my_account.password)
    rtoken = acc.refreshToken
    token = acc.token
    acc2 = apiAC.post_refreshToken(acc)
    assert rtoken != acc2.refreshToken and token != acc2.token






