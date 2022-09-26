import json
from Models.author import Author
import requests


class AuthorApi:
    def __init__(self, url: str = "http://localhost:7017/api/Authors"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_authors(self):
        res = self._session.get(url=f"{self._url}", headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = Author(**a1)
            return my_auth
        else:
            return res.status_code

    def post_authors(self, author: Author):
        author_data = json.dumps(author)
        res = self._session.post(url=f"{self._url}", data=author_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = Author(**a1)
            return my_auth
        else:
            return res.status_code

    def get_authors_by_id(self, id:int):
        res = self._session.get(url=f"{self._url}/{id}", headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = Author(**a1)
            return my_auth
        else:
            return res.status_code
