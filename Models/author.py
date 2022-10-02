from dataclasses import dataclass
from Models.baseObj import baseObj


@dataclass
class Author(baseObj):
    id: int
    name: str
    homeLatitude: float
    homeLongitude: float
    books: []

