import datetime

from Projet_Dev2.libs.classes.witness import Witness


class Victim(Witness):
    """A class for the victims of the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime.date = datetime.date.today(),
                 gender: str = '', testimony: str = '', contact: str = '', condition: str = '',
                 circumstance: str = ''):
        super().__init__(lastname, firstname, birthdate, gender, testimony, contact)
        self.__condition = condition
        self.__circumstance = circumstance

    @property
    def condition(self):
        """
        :post: Returns a description of the condition of the victim
        """
        return self.__condition

    @property
    def circumstance(self):
        """
        :post: Returns a description of the circumstances of the victim when the crime took place
        """
        return self.__circumstance
