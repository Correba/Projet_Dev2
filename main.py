"""
    Group members:
    - BRUGGER Alexandre
    - TROONBEECKX Hugo
    - VERBIEST Mateo
"""
import datetime


class EmptyValue(Exception):
    """An error for an empty value"""
    super()


class Investigation:
    """A class to represent a police investigation"""

    def __init__(self, name: str, status: str = 'In progress'):
        """
        :pre:
        - name : The name of the investigation
        - status : The current status of the investigation
        :post: Sets the attributes of the class to the given values
        """
        self.__name = name
        self.__evidence = []
        self.__status = status

    @property
    def name(self):
        """
        :post: Returns the name of the investigation
        """
        return self.__name

    @property
    def evidence(self):
        """
        :post: Returns the list of evidence of the investigation
        """
        return self.__evidence

    def add_evidence(self, evidence):
        """
        :pre: An evidence of the investigation
        :post: Adds a new evidence to the list of evidences
        """
        self.__evidence.append(evidence)

    @property
    def status(self):
        """
        :post: Returns the status of the investigation
        """
        return self.__status

    @status.setter
    def status(self, status: str):
        """
        :pre: A new status to set to an investigation
        :post: Sets the status to the investigation
        """
        self.__status = status

    def __str__(self):
        return f'Nom: {self.__name}, preuve: {self.__evidence}, etat: {self.__status}'


class Evidence:
    """A class of evidences found in a police investigation"""

    def __init__(self, name: str, description: str = '', date: datetime = datetime.date.today(), file: str = ''):
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
        self.__date = date
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


class Recording(Evidence):
    """A class for recording type evidences"""

    def __init__(self, name: str, description: str = '', date: datetime = datetime.date.today(),
                 file: str = '', recording_type: str = ''):
        super().__init__(name, description, date, file)
        if recording_type == '':
            raise EmptyValue('Missing type of recording')

        if recording_type in ['audio', 'video']:
            self.__recording_type = recording_type
        else:
            raise ValueError('Incorrect recording type')

    @property
    def recording_type(self):
        """
        The type of file of the recording
        :post: Returns the type of recording
        """
        return self.__recording_type


class Object(Evidence):
    """A class for object like evidences"""

    def __init__(self, name, description='', date=datetime.date.today(), file='', location=''):
        super().__init__(name, description, date, file)
        self.__location = location

    @property
    def location(self):
        """
        Get the location of the evidence
        :post: Returns the location where the object was found
        """
        return self.__location


class Picture(Object):
    """A class for pictures taken during the investigation"""
    def __init__(self, name, description='', date=datetime.date.today(), file='', location=''):
        super().__init__(name, description, date, file, location)
