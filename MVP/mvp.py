"""Module pour utiliser des options en ligne de commande"""
import argparse
import pickle

dict_enquete = {}
FICHIER_SAUVEGARDE = 'enquete_data.bin'


class Enquete:
    """
    POST : Un objet où stocké toutes les informations d'une enquête
    """

    def __init__(self, nom: str):
        self.__nom = nom
        self.__preuve = []
        self.__etat = 'En cours'

    @property
    def nom(self):
        """
        POST : Revoie la nom de l'enquête
        """
        return self.__nom

    @property
    def preuve(self):
        """
        POST : Renvoie la liste des preuves de l'enquête
        """
        return self.__preuve

    @preuve.setter
    def preuve(self, preuve):
        """
        PRE : Une preuve à ajouter à l'enquête
        POST : Ajoute une preuve à la liste des preuves de l'enquête
        """
        self.__preuve.append(preuve)

    @property
    def etat(self):
        """
        POST : Renvoie l'état de l'enquête
        """
        return self.__etat

    @etat.setter
    def etat(self, etat: str):
        """
        PRE : L'état a assigner a une enquête
        POST : Assigne un nouvelle état a l'enquête
        """
        self.__etat = etat

    def __str__(self):
        return f'Nom: {self.__nom}, preuve: {self.__preuve}, etat: {self.__etat}'


def save_object(obj, filename):
    """
    PRE : - obj est un objet a sauvegarder
          - filename est un fichier où sauvegarder un objet
    POST : Sauvegarde un objet dans un fichier
    """
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ce programme permet d\'encoder des nouvelles enquêtes et d\'encoder des preuves dans une enquête en particulier. Il permet également d\'afficher toutes les enquêtes ainsi que leur informations respectives.')
    parser.add_argument('--name', type=str, metavar='name',
                        help='le nom de l\'enquête a créer ou le nom de l\'enquête où il faut ajouter une preuve')
    parser.add_argument('--affichage', action='store_true',
                        help='affiche les enquêtes et leurs informations respectives')
    parser.add_argument('--preuve', metavar='preuve',
                        help='le nom de la preuve qui est ajoutée à une enquête choisie avec --name')

    args = parser.parse_args()

    try:
        with open(FICHIER_SAUVEGARDE, 'rb') as input_file:
            dict_enquete = pickle.load(input_file)

    except FileNotFoundError:
        pass
    except IOError:
        print('Erreur IO')

    if args.name:
        if args.preuve:
            try:
                dict_enquete[args.name].preuve.append(args.preuve)
                save_object(dict_enquete, FICHIER_SAUVEGARDE)
            except KeyError:
                print(f'L\'enquête {args.name} n\'existe pas')
        else:
            if args.name not in list(dict_enquete.keys()):
                dict_enquete[args.name] = Enquete(args.name)
                save_object(dict_enquete, FICHIER_SAUVEGARDE)
            else:
                print(f'L\'enquête {args.name} existe déjà')
    elif not args.affichage:
        print('Aucune enquête choisie')

    if args.affichage:
        if len(dict_enquete) != 0:
            for enquete in dict_enquete.keys():
                print(dict_enquete[enquete])
        else:
            print('Aucune enquête trouver')
