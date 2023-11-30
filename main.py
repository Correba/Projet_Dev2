"""import nécessaire au script"""
import pickle

import eel

INVESTIGATIONS = {}
BACKUP_FILE = 'investigations_data.bin'


# from libs.classes.investigation import *

def save_object(obj, filename):
    """
    :pre:
    - obj is the object to save
    - filename is the file where the object is saved
    :post: save an object in a file
    """
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    eel.init('web')

    eel.start('index.html', mode="browser")
