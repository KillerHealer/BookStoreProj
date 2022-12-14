from dataclasses import dataclass
from Models.author import Author
from Models.baseObj import baseObj


@dataclass
class Book(baseObj):
    id: int
    name: str
    description: str
    price: float
    amountInStock: int
    imageUrl: str
    authorId: int
    author: Author