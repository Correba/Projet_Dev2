import datetime

from Projet_Dev2.libs.classes.object import Object


class Picture(Object):
    """A class for pictures taken during the investigation"""

    def __init__(self, name, description='', date=datetime.date.today(), file='', location=''):
        super().__init__(name, description, date, file, location)
