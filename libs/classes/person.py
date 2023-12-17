import datetime

from .empty_value import EmptyValue


class Person:
    """A class for people involved in the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime.date = datetime.date.today(),
                 gender: str = ''):
        """
        :pre:
        - lastname : The lastname of the person
        - firstname : The firstname of the person
        - birthdate : The date the person was born
        - gender : The gender of the person
        """
        if lastname:
            self.__lastname = lastname
        else:
            raise EmptyValue('Lastname cannot be empty')

        if firstname:
            self.__firstname = firstname
        else:
            raise EmptyValue('Firstname cannot be empty')

        if birthdate <= datetime.date.today():
            self.__birthdate = birthdate
        else:
            raise ValueError('Birthdate cannot be in the future')
        self.__gender = gender

    @property
    def lastname(self):
        """
        :post: Returns the lastname of the person
        """
        return self.__lastname

    @property
    def firstname(self):
        """
        :post: Returns the firstname of the person
        """
        return self.__firstname

    @property
    def birthdate(self):
        """
        :post: Returns the birthdate of the person
        """
        return self.__birthdate

    @property
    def gender(self):
        """
        :post: Returns the gender of the person
        """
        return self.__gender
