

class AuthResponseDto:
    def __init__(self, userId: str, token: str, refreshToken: str):
        self._userId = userId
        self._token = token
        self._refreshToken = refreshToken


