

class AuthResponseDto:
    def __init__(self, userId: str, token: str, refreshToken: str):
        self._userId = userId
        self._token = token
        self._refreshToken = refreshToken

    @property
    def userId(self):
        """Gets the userId of this AuthResponseDto.
        :return: The userId of this AuthResponseDto.
        :type: str
        """
        return self._userId

    @userId.setter
    def userId(self, userId):
        """Sets the userId of this AuthResponseDto.
        :param userId: The userId of this AuthResponseDto.
        :type: str
        """
        self._userId = userId

    @property
    def token(self):
        """Gets the token of this AuthResponseDto.
        :return: The token of this AuthResponseDto.
        :type: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AuthResponseDto.
        :param token: The token of this AuthResponseDto.
        :type: str
        """
        self._token = token

    @property
    def refreshToken(self):
        """Gets the refreshToken of this AuthResponseDto.
        :return: The refreshToken of this AuthResponseDto.
        :type: str
        """
        return self._refreshToken

    @refreshToken.setter
    def refreshToken(self, refreshToken):
        """Sets the refreshToken of this AuthResponseDto.
        :param userId: The refreshToken of this AuthResponseDto.
        :type: str
        """
        self._refreshToken = refreshToken