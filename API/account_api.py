import json

from Models.account import Account
from Models.authResponseDto import AuthResponseDto
import requests


class AccountApi:
    def __init__(self, url: str = "http://localhost:7017/swagger/index.html/api/Account/"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_register(self, account: Account):
        account_data = account.to_json()
        res = self._session.post(url=f"{self._url}/register", data=account.__str__(), headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
           pass

    def post_login(self, email: str, password: str):
        account_data = {"email": email,
                        "password": password}
        res = self._session.post(url=f"{self._url}/login", data=account_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_acc = Account(**a1)
            return my_acc
        else:
            return res.status_code

    def post_refreshToken(self, email: str, password: str):
        account_data = {"email": email,
                        "password": password}
        res = self._session.post(url=f"{self._url}/refreshtoken", data=account_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_acc = Account(**a1)
            return my_acc
        else:
            return res.status_code

