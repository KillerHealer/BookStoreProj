import json
from Models.book import Book
from Models.bookdto import BookDto
import requests


class BookApi:
    def __init__(self, url: str = "http://localhost:7017/api/Books/"):
        self._url = url
        self._headers = {'accept': '*/*', 'content-Type': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_books(self):
        res = self._session.get(url=f"{self._url}", headers=self._headers)
        a1 = res.json()
        my_book = []
        if res.status_code == 200:
            for book in a1:
                my_book.append(BookDto(**book))
            return my_book
        else:
            return res.status_code

    def post_book(self, book: BookDto, bearerToken):
        book_data = book.to_json()
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.post(url=f"{self._url}", data=book_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 201:
            my_book = BookDto(**a1)
            return my_book
        else:
            return res.status_code

    def get_books_by_id(self, id):
        res = self._session.get(url=f"{self._url}/{id}", headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_book = BookDto(**a1)
            return my_book
        else:
            return res.status_code

    def put_book(self, book: Book, bearerToken):
        book_data = book.to_json()
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.put(url=f"{self._url}/{book.id}", data=book_data, headers=self._headers)
        if res.status_code == 204 or res.status_code == 200:
            return True
        else:
            return res.status_code

    def delete_book(self, id: int, bearerToken):
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.delete(url=f"{self._url}/{id}", headers=self._headers)
        a1 = res.json()
        if res.status_code == 201:
            my_book = BookDto(**a1)
            return my_book
        else:
            return res.status_code
