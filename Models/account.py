from Models.baseObj import baseObj


class Account(baseObj):
    def __init__(self, email: str, password: str, firstName: str, lastName: str):
        self._email = email
        self._password = password
        self._firstName = firstName
        self._lastName = lastName

    @property
    def email(self):
        """Gets the email of this Account.
        :return: The email of this Account.
        :type: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Account.
        :param email: The email of this Account.
        :type: str
        """
        self._email = email

    @property
    def password(self):
        """Gets the password of this Account.
        :return: The password of this Account.
        :type: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Account.
        :param password: The password of this Account.
        :type: str
        """
        self._password = password

    @property
    def firstName(self):
        """Gets the firstname of this Account.
        :return: The firstname of this Account.
        :type: str
        """
        return self._firstName

    @firstName.setter
    def firstName(self, firstname):
        """Sets the firstname of this Account.
        :param firstname: The firstname of this Account.
        :type: str
        """
        self._firstName = firstname

    @property
    def lastName(self):
        """Gets the lastName of this Account.
        :return: The lastName of this Account.
        :type: str
        """
        return self._lastName

    @lastName.setter
    def lastName(self, lastname):
        """Sets the lastname of this Account.
        :param lastname: The lastname of this Account.
        :type: str
        """
        self._lastName = lastname
