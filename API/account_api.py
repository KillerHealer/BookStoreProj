import json
from Models.account import Account
from Models.authResponseDto import AuthResponseDto
import requests


class AccountApi:
    def __init__(self, url: str = "http://localhost:7017/api/Account/"):
        self._url = url
        self._headers = {'accept': '*/*', 'content-Type': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_register(self, account: Account):
        account_data = account.to_json()
        res = self._session.post(url=f"{self._url}register", data=account_data, headers=self._headers)
        if res.status_code == 200:
            return True
        return False

    def post_login(self, email: str, password: str):
        account_data = {"email": email,
                        "password": password}
        account_data = json.dumps(account_data)
        res = self._session.post(url=f"{self._url}login", data=account_data, headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = AuthResponseDto(**a1)
            return my_auth
        else:
            return res.status_code

    def post_refreshToken(self, auth: AuthResponseDto):
        res = self._session.post(url=f"{self._url}refreshtoken", data=auth.to_json(), headers=self._headers)
        a1 = res.json()
        if res.status_code == 200:
            my_auth = AuthResponseDto(**a1)
            return my_auth
        else:
            return res.status_code
