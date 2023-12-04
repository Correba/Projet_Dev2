"""Module to use html as a GUI"""

import pickle

import eel

from libs.classes.investigation import *

eel.init('web')

INVESTIGATIONS = {}
BACKUP_FILE = 'investigations_data.bin'


def save_object():
    """
    POST: save an INVESTIGATIONS in BACKUP_FILE
    """
    with open(BACKUP_FILE, 'wb') as output:
        pickle.dump(INVESTIGATIONS, output, pickle.HIGHEST_PROTOCOL)


def read_save_file():
    try:
        with open(BACKUP_FILE, 'rb') as input_file:
            global INVESTIGATIONS
            INVESTIGATIONS = pickle.load(input_file)
    except FileNotFoundError:
        print('File not found')


@eel.expose
def create_investigations(element):
    INVESTIGATIONS[element] = Investigation(element)
    save_object()
    # table_investigations()


@eel.expose
def table_investigations():
    investigation_id = "investigationContent"
    html = "<tr>test</tr>"
    eel.addElement(investigation_id, html)


if __name__ == '__main__':
    read_save_file()
    eel.start('index.html', mode="browser")
