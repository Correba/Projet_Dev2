"""Module to use html as a GUI"""
import datetime
import pickle
import eel

from Projet_Dev2.libs.classes.culprit import Culprit
from Projet_Dev2.libs.classes.empty_value import EmptyValue
from Projet_Dev2.libs.classes.object import Object
from Projet_Dev2.libs.classes.picture import Picture
from Projet_Dev2.libs.classes.investigation import Investigation
from Projet_Dev2.libs.classes.evidence import Evidence
from Projet_Dev2.libs.classes.person import Person
from Projet_Dev2.libs.classes.recording import Recording
from Projet_Dev2.libs.classes.suspect import Suspect
from Projet_Dev2.libs.classes.victim import Victim
from Projet_Dev2.libs.classes.witness import Witness

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
    """
    :post:
    - save an INVESTIGATIONS in BACKUP_FILE
    - fill the HTML table with the content of the BACKUP_FILE
    """
    save_object()
    fill_table_investigations()


@eel.expose
def create_investigations(element):
    """
    :pre: element is a string
    :post: create an investigation named element and adds it to INVESTIGATIONS
    """
    INVESTIGATIONS[element] = Investigation(element)
    update_investigation()
    return f'Investigation {element} created'


@eel.expose
def fill_investigations_table(args=None):
    """
    :pre: args is required by eel module but is not used
    :post: fill the HTML table with the content of BACKUP_FILE
    """
    read_save_file()
    html = ''
    select = ''
    for investigation in list(INVESTIGATIONS.values()):
        html += (f'<tr><td>{investigation.name}</td><td onclick="fillEvidence(\'{investigation.name}\', this)">'
                 f'{len(investigation.evidence)}</td><td onclick="fillPeople(\'{investigation.name}\', this)">'
                 f'{len(investigation.people)}</td><td>{investigation.status}</td></tr>')
        select += f'<option value="{investigation.name}">{investigation.name}</value>'
    eel.addElement('investigationContent', html)
    eel.addElement('evidence_select', select)
    eel.addElement('people_select', select)


@eel.expose
def fill_type_forms(args=None):
    """
    :pre:
    - args is required by eel module but is not used
    - called when the page is loaded
    :post: fill the HTML select object of the forms
    """
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
                new_id = 'people' + type_info.capitalize()
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
    """
    :pre:
    - chosen_type is a string
    - chosen_investigation is a string
    - data is a list containing all information related to an evidence
    - args is required by eel module but is not used
    :post: creates an Evidence or inheritor and adds it to the chosen_investigation in INVESTIGATIONS
    """
    name, description, date, file, *extra = data
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    try:
        match chosen_type:
            case 'picture':
                new_evidence = Picture(name, description, date, file, extra[0])
            case 'object':
                new_evidence = Object(name, description, date, file, extra[0])
            case 'recording':
                new_evidence = Recording(name, description, date, file, extra[0])
            case _:
                new_evidence = Evidence(name, description, date, file)
        INVESTIGATIONS[chosen_investigation].add_evidence(new_evidence)
        update_investigation()
        return f'Evidence {name} created'
    except ValueError as value_error:
        return f'Invalid:{value_error}'
    except EmptyValue as empty_error:
        return f'Invalid:{empty_error}'


@eel.expose
def make_person(chosen_type: str, chosen_investigation: str, data: list, args=None):
    """
    :pre:
    - chosen_type is a string
    - chosen_investigation is a string
    - data is a list containing all information related to a person
    - args is required by eel module but is not used
    :post: creates a Person or inheritor and adds it to the chosen_investigation in INVESTIGATIONS
    """
    lastname, firstname, birthdate, gender, *extra = data
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    try:
        match chosen_type:
            case 'suspect':
                new_person = Suspect(lastname, firstname, birthdate, gender, extra[0], extra[1], extra[2])
            case 'culprit':
                new_person = Culprit(lastname, firstname, birthdate, gender, extra[0], extra[1], extra[2], extra[3],
                                     extra[4])
            case 'witness':
                new_person = Witness(lastname, firstname, birthdate, gender, extra[0], extra[1])
            case 'victim':
                new_person = Victim(lastname, firstname, birthdate, gender, extra[0], extra[1], extra[2], extra[3])
            case _:
                new_person = Person(lastname, firstname, birthdate, gender)
        INVESTIGATIONS[chosen_investigation].add_people(new_person)
        update_investigation()
        return f'Person {firstname} {lastname} created'
    except ValueError as value_error:
        return f'Invalid:{value_error}'
    except EmptyValue as empty_error:
        return f'Invalid:{empty_error}'


@eel.expose
def fill_evidence_table(chosen_investigation, args=None):
    html = ''
    for evidence in INVESTIGATIONS[chosen_investigation].evidence:
        match type(evidence):
            case Picture():
                evidence_type = 'Picture'
            case Object():
                evidence_type = 'Object'
            case Recording():
                evidence_type = 'Recording'
            case _:
                evidence_type = '/'
        html += (f'<tr><td>{evidence.name.capitalize()}</td><td>{evidence.description}</td><td>{evidence.date}</td>'
                 f'<td>{evidence_type}</td></tr>')
    eel.addElement('evidenceContent', html)


@eel.expose
def fill_people_table(chosen_investigation, args=None):
    html = ''
    for people in INVESTIGATIONS[chosen_investigation].people:
        match type(people):
            case Suspect():
                people_type = 'Suspect'
            case Culprit():
                people_type = 'Culprit'
            case Witness():
                people_type = 'Witness'
            case Victim():
                people_type = 'Victim'
            case _:
                people_type = '/'
        html += (f'<tr><td>{people.lastname.capitalize()}</td><td>{people.firstname.capitalize()}</td>'
                 f'<td>{people.birthdate}</td><td>{people.gender}</td><td>{people_type}</td></tr>')
    eel.addElement('peopleContent', html)


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
