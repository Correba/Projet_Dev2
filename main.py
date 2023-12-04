"""Module to use html as a GUI"""

import pickle
import eel
from libs.classes.investigation import *

eel.init('web')

INVESTIGATIONS = {}
BACKUP_FILE = 'investigations_data.bin'


def save_object():
    """
    :post: save an INVESTIGATIONS in BACKUP_FILE
    """
    with open(BACKUP_FILE, 'wb') as output:
        pickle.dump(INVESTIGATIONS, output, pickle.HIGHEST_PROTOCOL)


def read_save_file():
    """
    :post: initialize INVESTIGATIONS with the Investigations stored in BACKUP_FILE
    """
    try:
        with open(BACKUP_FILE, 'rb') as input_file:
            global INVESTIGATIONS
            INVESTIGATIONS = pickle.load(input_file)
    except FileNotFoundError:
        pass


@eel.expose
def create_investigations(element):
    INVESTIGATIONS[element] = Investigation(element)
    save_object()
    fill_table_investigations()


@eel.expose
def fill_table_investigations(args):
    read_save_file()
    html = ''
    select = ''
    for investigation in INVESTIGATIONS.values():
        html += f'<tr><td>{investigation.name.capitalize()}</td><td>{len(investigation.evidence)}</td><td>{len(investigation.people)}</td><td>{investigation.status}</td></tr>'
        select += f'<option value="{investigation.name}">{investigation.name.capitalize()}</value>'
    eel.addElement('investigationContent', html)
    eel.addElement('evidence_select', select)
    eel.addElement('people_select', select)


@eel.expose
def make_type_forms(args):
    evidence_types = {'picture': ['location'], 'object': ['location'], 'recording': [['audio', 'video']]}
    person_types = {'suspect': ['picture', 'suspicion', 'criminal_record'], 
                    'culprit': ['picture', 'suspicion', 'criminal record', 'motivation', 'victim_relationship'],
                    'witness': ['testimony', 'contact'], 'victim': ['testimony', 'contact', 'condition', 'circumstance']}
    evidence_select = '<option value="default" selected><---!---></option>'
    person_select = evidence_select
    for evidence in list(evidence_types.keys()):
        evidence_select += f'<option value"{evidence}">{evidence.capitalize()}</option>'
    for person in list(person_types.keys()):
        person_select += f'<option value"{person}">{person.capitalize()}</option>'
    eel.addElement('evidenceType', evidence_select)
    eel.addElement('peopleType', person_select)


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
