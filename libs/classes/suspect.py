import datetime

from person import Person


class Suspect(Person):
    """A class for the suspects of the investigation"""

    def __init__(self, lastname: str, firstname: str, birthdate: datetime.date = datetime.date.today(),
                 gender: str = '', picture: str = '', suspicion: str = '', criminal_record: str = ''):
        super().__init__(lastname, firstname, birthdate, gender)
        self.__picture = picture
        self.__suspicion = suspicion
        self.__criminal_record = criminal_record

    @property
    def picture(self):
        """
        :post: Returns a picture of the suspect
        """
        return self.__picture

    @property
    def suspicion(self):
        """
        :post: Returns a description of why the person is a suspect in the investigation
        """
        return self.__suspicion

    @property
    def criminal_record(self):
        """
        :post: Returns the criminal record of the suspect
        """
        return self.__criminal_record
