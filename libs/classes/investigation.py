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
        self.__people = []
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
    def people(self):
        """
        :post: Returns the list of people of the investigation
        """
        return self.__evidence

    def add_people(self, people):
        """
        :pre: An people of the investigation
        :post: Adds a new people to the list of evidences
        """
        self.__people.append(people)

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
        return f'Name: {self.__name}, proof: {self.__evidence}, person: {self.__people}, status: {self.__status}'
