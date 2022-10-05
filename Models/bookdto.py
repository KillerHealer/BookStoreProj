from dataclasses import dataclass
from Models.baseObj import baseObj


@dataclass
class BookDto(baseObj):
    id: int
    name: str
    description: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
