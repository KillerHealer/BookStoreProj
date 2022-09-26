from Models.baseObj import baseObj


class Author(baseObj):
    def __init__(self, id: int, name: str,
                 homeLatitude: float, homeLongitude: float):
        self._id = id
        self._name = name
        self._homeLatitude = homeLatitude
        self._homeLongitude = homeLongitude

    @property
    def id(self):
        """Gets the id of this Author.
        :return: The id of this Author.
        :type: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Author.
        :param id: The id of this Author.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Author.
        :return: The name of this Author.
        :type: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Author.
        :param name: The name of this Author.
        :type: str
        """
        self._name = name

    @property
    def homeLatitude(self):
        """Gets the homeLatitude of this Author.
        :return: The homeLatitude of this Author.
        :type: float
        """
        return self._homeLatitude

    @homeLatitude.setter
    def homeLatitude(self, homeLatitude):
        """Sets the homeLatitude of this Author.
        :param homeLatitude: The homeLatitude of this Author.
        :type: float
        """
        self._homeLatitude = homeLatitude

    @property
    def homeLongitude(self):
        """Gets the homeLongitude of this Author.
        :return: The homeLongitude of this Author.
        :type: float
        """
        return self._homeLongitude

    @homeLongitude.setter
    def homeLongitude(self, homeLongitude):
        """Sets the homeLongitude of this Author.
        :param homeLongitude: The homeLongitude of this Author.
        :type: float
        """
        self._homeLongitude = homeLongitude


