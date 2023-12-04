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
    table_investigations()


@eel.expose
def table_investigations(args):
    read_save_file()
    investigation_id = "investigationContent"
    evidence_select_id = 'evidence_select'
    people_select_id = 'people_select'
    html = ''
    select = ''
    for investigation in INVESTIGATIONS.values():
        html += f'<tr><td>{investigation.name.capitalize()}</td><td>{len(investigation.evidence)}</td><td>{len(investigation.people)}</td><td>{investigation.status}</td></tr>'
        select += f'<option value="{investigation.name}">{investigation.name.capitalize()}</value>'
    eel.addElement(investigation_id, html)
    eel.addElement(evidence_select_id, select)
    eel.addElement(people_select_id, select)


if __name__ == '__main__':
    eel.start('index.html', mode="browser")
