from dataclasses import dataclass
from Models.baseObj import baseObj

@dataclass
class Account(baseObj):
    email: str
    password: str
    firstName: str
    lastName: str