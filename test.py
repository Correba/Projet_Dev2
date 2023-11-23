from libs.classes import Investigation
import eel

investigation1 = Investigation("test1")

if __name__ == "__main__":
    eel.init('web')

    eel.start('index.html')