"""Module to use html as a GUI"""
import datetime
import pickle
import eel
from libs.classes.investigation import Investigation
from libs.classes.evidence import Evidence
from libs.classes.person import Person

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


def update_investigation():
    save_object()
    fill_table_investigations()


@eel.expose
def create_investigations(element):
    INVESTIGATIONS[element] = Investigation(element)
    update_investigation()


@eel.expose
def fill_table_investigations(args=None):
    read_save_file()
    html = ''
    select = ''
    for investigation in list(INVESTIGATIONS.values()):
        html += (f'<tr><td>{investigation.name}</td><td>{len(investigation.evidence)}</td>'
                 f'<td>{len(investigation.people)}</td><td>{investigation.status}</td></tr>')
        select += f'<option value="{investigation.name}">{investigation.name}</value>'
    eel.addElement('investigationContent', html)
    eel.addElement('evidence_select', select)
    eel.addElement('people_select', select)


@eel.expose
def fill_type_forms(args=None):
    evidence_types = ['picture', 'object', 'recording']
    person_types = ['suspect', 'culprit', 'witness', 'victim']
    evidence_select = person_select = '<option value="default" selected><---!---></option>'
    for evidence in evidence_types:
        evidence_select += f'<option value="{evidence}">{evidence.capitalize()}</option>'
    for person in person_types:
        person_select += f'<option value="{person}">{person.capitalize()}</option>'
    eel.addElement('evidenceType', evidence_select)
    eel.addElement('peopleType', person_select)


@eel.expose
def make_type_input(chosen_type: str, parent_id: str, args=None):
    """
    :pre:
    - chosen_type is a string
    - parent_id is a string
    - args is required by eel module but is not used
    :post: makes new HTML input tags in the HTML object identified by parent_id
    """
    type_input = ''
    chosen_element = parent_id.split('T')[0]
    return_id = chosen_element + 'Extra'
    evidence_types = {'picture': 'location', 'object': 'location', 'recording': 'recording'}
    person_types = {'suspect': ['picture', 'suspicion', 'criminal_record'],
                    'culprit': ['picture', 'suspicion', 'criminal_record', 'motivation', 'victim_relationship'],
                    'witness': ['testimony', 'contact'],
                    'victim': ['testimony', 'contact', 'condition', 'circumstance']}

    if chosen_type == 'default':
        eel.addElement(return_id, '')
        return

    match chosen_element:
        case 'evidence':
            new_id = 'evidence' + chosen_type.capitalize()
            type_input += f'<label for="{new_id}">{evidence_types[chosen_type].capitalize()} : </label><input '
            match chosen_type:
                case 'recording':
                    type_input += 'type="file" accept="audio/*, video/*" '
                case _:
                    type_input += 'type="text" '
            type_input += f'id="{new_id}" name="{new_id}" required><br>'
        case 'people':
            for type_info in person_types[chosen_type]:
                new_id = 'people' + chosen_type.capitalize() + type_info.capitalize()
                type_input += f'<label for="{new_id}">{type_info.capitalize()} : </label><input '
                match type_info:
                    case 'picture':
                        type_input += 'type="file" accept="image/*" '
                    case 'criminal_record':
                        type_input += 'type="file" '
                    case _:
                        type_input += 'type="text" '
                type_input += f'id="{new_id}" name="{new_id}" required><br>'
    eel.addElement(return_id, type_input)


@eel.expose
def make_evidence(chosen_type: str, chosen_investigation: str, data: list, args=None):
    name, description, date, file, *extra = data
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    new_evidence = None
    match chosen_type:
        case 'picture':
            pass
        case 'object':
            pass
        case 'recording':
            pass
        case _:
            new_evidence = Evidence(name, description, date, file)
    INVESTIGATIONS[chosen_investigation].add_evidence(new_evidence)
    update_investigation()


@eel.expose
def make_person(chosen_type: str, chosen_investigation: str, data: list, args=None):
    firstname, lastname, birthdate, gender, *extra = data
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    new_person = None
    match chosen_type:
        case 'picture':
            pass
        case 'object':
            pass
        case 'recording':
            pass
        case _:
            new_person = Person(firstname, lastname, birthdate, gender)
    INVESTIGATIONS[chosen_investigation].add_people(new_person)
    update_investigation()


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
