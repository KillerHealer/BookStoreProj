from Models.author import Author
from Models.baseObj import baseObj


class Book(baseObj):
    def __init__(self, id: int, name: str, description: str, price: float,
                 amountInStock: int, imageUrl: str, authorId: int, author: Author):
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId
        self._author = author

    @property
    def id(self):
        """Gets the id of this Book.
        :return: The id of this Book.
        :type: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Book.
        :param id: The id of this Book.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Book.
        :return: The name of this Book.
        :type: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Book.
        :param name: The name of this Book.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Book.
        :return: The description of this Book.
        :type: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Book.
        :param description: The description of this Book.
        :type: str
        """
        self._description = description

    @property
    def price(self):
        """Gets the price of this Book.
        :return: The price of this Book.
        :type: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Book.
        :param price: The price of this Book.
        :type: float
        """
        self._price = price

    @property
    def amountInStock(self):
        """Gets the amountInStock of this Book.
        :return: The amountInStock of this Book.
        :type: int
        """
        return self._amountInStock

    @amountInStock.setter
    def amountInStock(self, amountInStock):
        """Sets the amountInStock of this Book.
        :param amountInStock: The amountInStock of this Book.
        :type: int
        """
        self._amountInStock = amountInStock

    @property
    def imageUrl(self):
        """Gets the imageUrl of this Book.
        :return: The imageUrl of this Book.
        :type: str
        """
        return self._imageUrl

    @imageUrl.setter
    def imageUrl(self, imageUrl):
        """Sets the imageUrl of this Book.
        :param imageUrl: The imageUrl of this Book.
        :type: str
        """
        self._imageUrl = imageUrl

    @property
    def authorId(self):
        """Gets the authorId of this Book.
        :return: The authorId of this Book.
        :type: int
        """
        return self._authorId

    @authorId.setter
    def authorId(self, authorId):
        """Sets the authorId of this Book.
        :param authorId: The authorId of this Book.
        :type: int
        """
        self._authorId = authorId

    @property
    def author(self):
        """Gets the author of this Book.
        :return: The author of this Book.
        :type: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Book.
        :param author: The author of this Book.
        :type: Author
        """
        self._author = author
