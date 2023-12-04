"""Module to use html as a GUI"""

import pickle

import eel

INVESTIGATIONS = {}
BACKUP_FILE = 'investigations_data.bin'


# from libs.classes.investigation import *

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


if __name__ == "__main__":
    eel.init('web')

    eel.start('index.html', mode="browser")
