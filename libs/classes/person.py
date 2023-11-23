import datetime


class Person:
    """A class for people ivolved in the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime = datetime.date.today(),
                 gender: str = ''):
        """
        :pre:
        - lastname : The lastname of the person
        - firstname : The firstname of the person
        - birthdate : The date the person was born
        - gender : The gender of the person
        """
        self.__lastname = lastname
        self.__firstname = firstname
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
