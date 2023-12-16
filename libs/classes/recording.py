import datetime

from Projet_Dev2.libs.classes.evidence import Evidence
from Projet_Dev2.libs.classes.empty_value import EmptyValue


class Recording(Evidence):
    """A class for recording type evidences"""

    def __init__(self, name: str, description: str = '', date: datetime.date = datetime.date.today(),
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
