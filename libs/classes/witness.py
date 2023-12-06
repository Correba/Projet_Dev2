import datetime

from person import Person


class Witness(Person):
    """A class for the witnesses of the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime.date = datetime.date.today(),
                 gender: str = '', testimony: str = '', contact: str = ''):
        super().__init__(lastname, firstname, birthdate, gender)
        self.__testimony = testimony
        self.__contact = contact

    @property
    def testimony(self):
        """
        :post: Returns the testimony of the witness
        """
        return self.__testimony

    @property
    def contact(self):
        """
        :post: Returns the witness contact
        """
        return self.__contact
