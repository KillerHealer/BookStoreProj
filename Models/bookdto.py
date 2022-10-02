from dataclasses import dataclass
from Models.baseObj import baseObj


@dataclass
class BookDto(baseObj):
    name: str
    description: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
