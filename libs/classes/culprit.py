import datetime

from .suspect import Suspect


class Culprit(Suspect):
    """A class for the culprits of the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime.date = datetime.date.today(),
                 gender: str = '', picture: str = '', suspicion: str = '', criminal_record: str = '',
                 motivation: str = '', victim_relationship: str = ''):
        super().__init__(lastname, firstname, birthdate, gender, picture, suspicion, criminal_record)
        self.__motivation = motivation
        self.__victim_relationship = victim_relationship

    @property
    def motivation(self):
        """
        :post: Returns a description of why the culprit did the crime
        """
        return self.__motivation

    @property
    def victim_relationship(self):
        """
        :post: Returns a description of how the culprit knows the victim
        """
        return self.__victim_relationship
