import pytest
import logging
from API.account_api import AccountApi
from Models.account import Account
from Models.authResponseDto import AuthResponseDto
from API.book_api import BookApi
from API.author_api import AuthorApi
import time
from Models.author import Author
from Models.book import Book
from Models.bookdto import BookDto

my_account = Account(f"hhh{int(time.time())}@example.com", "123456", "noam", "barkai")
my_author = Author(int(time.time()), f"noam", 10.00, 20.22, [])
my_book = BookDto(int(time.time()), "ender", "good book i recommend", 50.0, 100, "", 4)
apiAC = AccountApi()
apiAU = AuthorApi()
apiB = BookApi()


@pytest.mark.account()
def test_post_account_register():
    """
    tries to register a new account to the system
    :return:
    """
    global my_account
    logging.info("trying to add a new account")
    assert apiAC.post_register(my_account)
    acc = apiAC.post_login(my_account.email, my_account.password)
    assert isinstance(acc, AuthResponseDto)


@pytest.mark.account()
def test_post_account_refreshtoken():
    """
    logs in and uses that information to activate refreshtoken
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    rtoken = acc.refreshToken
    token = acc.token
    acc2 = apiAC.post_refreshToken(acc)
    assert rtoken != acc2.refreshToken and token != acc2.token


@pytest.mark.author()
def test_post_author():
    """
    logs in, authorize with token,
    tries to post an author and tries to find it by id
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    author = apiAU.post_author(my_author, acc2.token)
    assert isinstance(author, Author)
    assert author.id == apiAU.get_authors_by_id(author.id).id


@pytest.mark.author()
def test_put_author():
    """
    logs in, authorize with token and tries to update an author
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    author = apiAU.post_author(my_author, acc2.token)
    author.name = "Barkai"
    author.homeLongitude = -11.11
    assert apiAU.put_author(author, acc2.token)
    assert author.homeLongitude == apiAU.get_authors_by_id(author.id).homeLongitude


@pytest.mark.book()
def test_post_book():
    """
    Log in, authorize with token and tries to post book and find it by id
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    book = apiB.post_book(my_book, acc2.token)
    assert isinstance(book, Book)
    time.sleep(5)
    assert book.id == apiB.get_books_by_id(book.id).id


@pytest.mark.book()
def test_put_book():
    """
    Log in, authorize with token and tries to update book and find it by id
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    book = apiB.post_book(my_book, acc2.token)
    book.name = "Ender new"
    book.price = 55
    assert apiB.put_book(book, acc2.token)
    assert book.id == apiB.get_books_by_id(book.id).id


@pytest.mark.book()
def test_delete_book():
    """
    Log in, authorize with ADMIN token and tries to delete book and not find it by id
    :return:
    """
    acc = apiAC.post_login("admin@sela.co.il", "ADMIN")
    acc2 = apiAC.post_refreshToken(acc)
    my_new_book = apiB.post_book(my_book, acc2.token)
    assert apiB.delete_book(my_new_book.id, acc2.token)
    alert_code = apiB.get_books_by_id(my_new_book.id)
    assert alert_code == 404


@pytest.mark.book()
def test_find_book_by_authorid():
    """
    makes a new author, a new book and tries to find a book by its author's id
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    booli = False
    author = apiAU.post_author(Author(5, f"noam", 10.00, 20.22, []), acc2.token)
    my_book.authorId = author.id
    book = apiB.post_book(my_book, acc2.token)
    books = apiB.get_book_by_author(author.id)
    for book_a in books:
        if book_a.id == book.id:
            booli = True
    assert booli


@pytest.mark.book()
def test_purchase_book():
    """
    purchases a book and checks the stock before and after
    :return:
    """
    acc = apiAC.post_login("hhh1@example.com", "123456")
    acc2 = apiAC.post_refreshToken(acc)
    stockB = apiB.get_books_by_id(1).amountInStock
    book = apiB.purchase_book(1, acc2.token)
    assert stockB - 1 == book.amountInStock

