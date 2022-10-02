from dataclasses import dataclass
from Models.baseObj import baseObj


@dataclass
class AuthResponseDto(baseObj):
    userId: str
    token: str
    refreshToken: str

