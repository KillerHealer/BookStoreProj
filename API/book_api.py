import json
from Models.book import Book
import requests


class BookApi:
    def __init__(self, url: str = "http://localhost:7017/api/Books/"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

