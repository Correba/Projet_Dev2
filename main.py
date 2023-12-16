"""Module to use html as a GUI"""
import datetime
import pickle
import eel
import re
import os

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


def use_regex(input_text):
    """
    :pre: input_text is a string
    :post: return the input_text if input_text matches the regex pattern else return None
    """
    pattern = re.compile(r".*investigations_data.*\.bin")
    return pattern.match(input_text)


def gen_backup_file():
    """
    :post: yield the name of the backup_file if it exists
    """
    for file in os.listdir('./'):
        if use_regex(file):
            yield file


def save_object():
    """
    :post: save INVESTIGATIONS in backup_file
    """
    backup_file = gen_backup_file()  # generator and regex

    while True:
        try:
            with open(next(backup_file), 'wb') as output:
                pickle.dump(INVESTIGATIONS, output, pickle.HIGHEST_PROTOCOL)
                break
        except FileNotFoundError:
            pass
        except IOError:
            pass
        except StopIteration:
            with open('investigations_data.bin', 'wb') as output:
                pickle.dump(INVESTIGATIONS, output, pickle.HIGHEST_PROTOCOL)
            break


def read_save_file():
    """
    :post: initialize INVESTIGATIONS with the Investigations stored in backup_file
    """
    backup_file = gen_backup_file()  # generator and regex
    while True:
        try:
            with open(next(backup_file) if backup_file else '', 'rb') as input_file:
                global INVESTIGATIONS
                INVESTIGATIONS = pickle.load(input_file)
                break
        except FileNotFoundError:
            pass
        except IOError:
            pass
        except StopIteration:
            break


def update_investigation():
    """
    :post:
    - save an INVESTIGATIONS in backup_file
    - fill the HTML table with the content of the backup_file
    """
    save_object()
    fill_investigations_table()


@eel.expose
def create_investigations(element: str, status: str, args=None):
    """
    :pre: element is a string
    :post: create an investigation named element and adds it to INVESTIGATIONS
    """
    element = str.capitalize(element)
    if element in INVESTIGATIONS:
        INVESTIGATIONS[element].status = status
        update_investigation()
        return f'Investigation {element}\'s status changed to {status}'
    INVESTIGATIONS[element] = Investigation(element)
    INVESTIGATIONS[element].status = status
    update_investigation()
    return f'Investigation {element} created'


@eel.expose
def fill_investigations_table(chosen_investigations: str = None, args=None):
    """
    :pre: args is required by eel module but is not used
    :post: fill the HTML table with the content of backup_file
    """
    read_save_file()
    if not chosen_investigations:
        chosen_investigations = INVESTIGATIONS
    html = ''
    select = ''
    for investigation in list(chosen_investigations.values()):
        html += (f'<tr id="{investigation.name}" onclick="selectInvestigation(this)"><td>{investigation.name}</td>'
                 f'<td onclick="fillEvidencePeople(\'{investigation.name}\')">{len(investigation.evidence)}</td>'
                 f'<td onclick="fillEvidencePeople(\'{investigation.name}\')">{len(investigation.people)}</td>'
                 f'<td onclick="filterStatus(\'{investigation.status}\', \'{investigation.name}\')">'
                 f'{investigation.status}</td></tr>')
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
        eel.clearElement(return_id)
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
    name = str.capitalize(name)
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
    lastname, firstname = map(str.capitalize, [lastname, firstname])
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
        html += (f'<tr><td>{people.lastname}</td><td>{people.firstname}</td><td>{people.birthdate}</td>'
                 f'<td>{people.gender}</td><td>{people_type}</td></tr>')
    eel.addElement('peopleContent', html)


@eel.expose
def sort_investigations(row, args=None):
    match row:
        case 'name':
            sorted_investigations = dict(sorted(INVESTIGATIONS.items(), key=lambda x: x[1].name))
        case 'status':
            sorted_investigations = dict(sorted(INVESTIGATIONS.items(), key=lambda x: x[1].status))
        case 'evidence':
            sorted_investigations = dict(sorted(INVESTIGATIONS.items(), key=lambda x: len(x[1].evidence), reverse=True))
        case 'people':
            sorted_investigations = dict(sorted(INVESTIGATIONS.items(), key=lambda x: len(x[1].people), reverse=True))
    eel.clearElement('investigationContent')
    fill_investigations_table(sorted_investigations)


@eel.expose
def filter_status(status, args=None):
    filtered_investigations = dict(filter(lambda x: x[1].status == status, INVESTIGATIONS.items()))
    eel.clearElement('investigationContent')
    fill_investigations_table(filtered_investigations)
    return True


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
