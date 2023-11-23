import datetime

from evidence import Evidence


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
