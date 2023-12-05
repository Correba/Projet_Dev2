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
def fill_table_investigations(args=None):
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
def fill_type_forms(args=None):
    evidence_types = ['picture', 'object', 'recording']
    person_types = ['suspect', 'culprit', 'witness', 'victim']
    evidence_select = '<option value="default" selected><---!---></option>'
    person_select = evidence_select
    for evidence in evidence_types:
        evidence_select += f'<option value"{evidence}">{evidence.capitalize()}</option>'
    for person in person_types:
        person_select += f'<option value"{person}">{person.capitalize()}</option>'
    eel.addElement('evidenceType', evidence_select)
    eel.addElement('peopleType', person_select)


@eel.expose
def make_type_input(type: str, parent_id: str, args=None):
    type_input = ''
    type = type.lower()
    return_id = parent_id.split('T')[0] + 'Extra'
    evidence_types = {'picture': 'location', 'object': 'location', 'recording': 'recording'}
    person_types = {'suspect': ['picture', 'suspicion', 'criminal_record'],
                    'culprit': ['picture', 'suspicion', 'criminal_record', 'motivation', 'victim_relationship'],
                    'witness': ['testimony', 'contact'],
                    'victim': ['testimony', 'contact', 'condition', 'circumstance']}

    if type == 'default':
        eel.addElement(return_id, '')
    elif 'evidence' in parent_id:
        new_id = 'evidence' + type.capitalize()
        type_input += f'<label for="{new_id}">{evidence_types[type].capitalize()} : </label>'
        if type == 'recording':
            type_input += f'<input type="file" accept="audio/*, video/*" id="{new_id}" name="{new_id}" required><br>'
        else:
            type_input += f'<input type="text" id="{new_id}" name="{new_id}" required><br>'
    elif 'people' in parent_id:
        for type_info in person_types[type]:
            new_id = 'people' + type.capitalize() + type_info.capitalize()
            type_input += f'<label for="{new_id}">{type_info.capitalize()} : </label>'
            if type_info == 'picture':
                type_input += f'<input type="file" accept="image/*" id="{new_id}" name="{new_id}" required><br>'
            elif type_info == 'criminal_record':
                type_input += f'<input type="file" id="{new_id}" name="{new_id}" required><br>'
            else:
                type_input += f'<input type="text" id="{new_id}" name="{new_id}" required><br>'

    eel.addElement(return_id, type_input)


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
