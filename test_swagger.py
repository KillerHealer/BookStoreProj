import pytest
import logging
import requests
from API.account_api import AccountApi
from Models.account import Account
from Models.authResponseDto import AuthResponseDto
from API.book_api import BookApi
from API.author_api import AuthorApi
my_account = Account("hhh@example.com", "123456", "noam", "barkai")
apiAC = AccountApi()
apiAU = AuthorApi()
apiB = BookApi()


@pytest.mark.account()
def test_post_account_register():
    """
    tries to register a new account to the system
    :return:
    """
    logging.info("trying to add a new account")
    acc = apiAC.post_register(my_account)
    assert isinstance(acc, Account)



