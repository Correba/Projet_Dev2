import datetime
from ..classes.empty_value import EmptyValue


class Evidence:
    """A class of evidences found in a police investigation"""

    def __init__(self, name: str, description: str = '', date: datetime.date = datetime.date.today(), file: str = ''):
        """
        :pre:
        - name : The name of the evidence
        - description : A short description of relevant information about the evidence
        - date : The date the evidence was found
        - file : The file of the evidence
        :raise: if name or the file is empty raises EmptyValue error
        """
        if name == '' or file == '':
            raise EmptyValue('No name set for the evidence')

        self.__name = name
        self.__description = description
        if date <= datetime.date.today():
            self.__date = date
        else:
            raise ValueError('Proof date cannot be in the future')
        self.__file = file

    @property
    def name(self):
        """
        :post: Returns the name of the investigation
        """
        return self.__name

    @property
    def description(self):
        """
        :post: Returns the description of the investigation
        """
        return self.__description

    @property
    def date(self):
        """
        :post: Returns the date of the investigation
        """
        return self.__date

    @property
    def file(self):
        """
        :post: Returns the file of the investigation
        """
        return self.__file
