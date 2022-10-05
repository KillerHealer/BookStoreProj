import json
from Models.author import Author
import requests


class AuthorApi:
    def __init__(self, url: str = "http://localhost:7017/api/Authors"):
        self._url = url
        self._headers = {'accept': '*/*', 'content-Type': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_authors(self) -> [Author] or int:
        res = self._session.get(url=f"{self._url}", headers=self._headers)
        a1 = res.json()
        my_auth = []
        if res.status_code == 200:
            for author in a1:
                my_auth.append(Author(**author))
            return my_auth
        else:
            return res.status_code

    def post_author(self, author: Author, bearerToken) -> Author or int:
        author_data = author.to_json()
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.post(url=f"{self._url}", data=author_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 201:
            my_auth = Author(**a1)
            return my_auth
        else:
            return res.status_code

    def get_authors_by_id(self, id: int) -> Author or int:
        res = self._session.get(url=f"{self._url}/{id}", headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = Author(**a1)
            return my_auth
        else:
            return res.status_code

    def put_author(self, author: Author, bearerToken) -> bool or int:
        author_data = author.to_json()
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.put(url=f"{self._url}/{author.id}", data=author_data, headers=self._headers)
        if res.status_code == 204 or res.status_code == 200:
            return True
        else:
            return res.status_code

    def delete_author(self, bearerToken, id: int) -> bool or int:
        self._headers['Authorization'] = f'Bearer {bearerToken}'
        res = self._session.put(url=f"{self._url}/{id}", headers=self._headers)
        if res.status_code == 204 or res.status_code == 200:
            return True
        else:
            return res.status_code

    def get_authors_by_text(self, sw: str) -> [Author] or int:
        res = self._session.get(url=f"{self._url}/search/{sw}", headers=self._headers)
        a1 = res.json()
        my_auth = []
        if res.status_code == 200:
            for author in a1:
                my_auth.append(Author(**author))
            return my_auth
        else:
            return res.status_code
