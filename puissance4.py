"""Module de la classe Puissance4

Classes:
    * Puissance4 - Classe pour encapsuler le jeu Puissance4.
"""

from copy import deepcopy
from puissance4_error import Puissance4_Error

class Puissance4:
    """Classe pour représenter le jeu Puissance 4.

    Attributes:
        * état (dict) - État actuel du jeu.
        * joueur (int) - Numéro du joueur dont c'est le tour.
        * tab (list) - Tableau contenant le nombre d'égalités,
          de victoires du joueur 1 et de victoires du joueur 2.
    """
    def __init__(self, joueurs, tab=None):
        """Constructeur de la classe Puissance 4.


        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            tab (List, optionnel): Un tableau de 3 entiers contenant respectivement 
            le nombre d'égalités, le nombre de victoires du joueur 1 et
            le nombre de victoires du joueur 2.
        """
        self.état = deepcopy(self.vérification(joueurs))
        self.actualiser()
        self.joueur = 1
        if tab is None:
            self.tab = [0, 0, 0]
        else:
            self.tab = tab

    def vérification(self, joueurs):
        """Vérifie si les joueurs sont valides.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
        
        Returns:
            Dict : Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.

        Raises:
            Puissance4_Error: L'argument 'joueurs' n'est pas itérable.
            Puissance4_Error: L'itérable de joueurs en contient un nombre différent de deux.
            Puissance4_Error: Le total des pions placés est atteint.
            Puissance4_Error: Un pion est placé en dehors du damier.
            Puissance4_Error: La position d'un pion est invalide.
        """
        # Vérification de l'itérabilité de l'argument joueurs
        if not hasattr(joueurs, '__iter__'):
            raise Puissance4_Error("L'argument 'joueurs' n'est pas itérable.")

        # Vérification du nombre de joueurs
        if len(joueurs) != 2:
            raise Puissance4_Error("L'itérable de joueurs en contient un nombre différent de deux.")

        #Si joueur est une chaîne de caractères
        if isinstance(joueurs[0], str) and isinstance(joueurs[1], str):
            joueur1 = {'nom': joueurs[0], 'pions' : [] }
            joueur2 = {'nom': joueurs[1], 'pions' : [] }

        else:
            pions = joueurs[0]['pions'] + joueurs[1]['pions']

            # Vérification du nombre total de murs
            if pions is not None and (len(joueurs[0]['pions']) +
                                     len(joueurs[1]['pions'])) > 32:
                raise Puissance4_Error("Le total des pions placés est atteint.")

            # Vérification de la position des murs
            if pions is not None:
                for pion in joueurs[0]['pions']:
                    if pion[0] < 1 or pion[0] > 7 or pion[1] < 1 or pion[1] > 6:
                        raise Puissance4_Error("La position d'un pion est invalide.")
                for pion in joueurs[1]['pions']:
                    if pion[0] < 1 or pion[0] > 7 or pion[1] < 1 or pion[1] > 6:
                        raise Puissance4_Error("La position d'un pion est invalide.")

            joueur1 = joueurs[0]
            joueur2 = joueurs[1]

        #Création de l'état
        etat = {'joueurs': [joueur1, joueur2]}

        return etat

    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)

    def est_terminée(self):
        """Déterminer si la partie est terminée.

        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        #La partie de puissance 4 est terminée
        rows = self.stockage_pions.get_size()[0]
        cols = self.stockage_pions.get_size()[1]
        # Vérification des lignes horizontales
        for col in range(rows):
            for row in range(cols - 3):
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col, row + 1]
                    == self.stockage_pions[col, row + 2]
                    == self.stockage_pions[col, row + 3]
                    == 'x'
                ):
                    return True
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col, row + 1]
                    == self.stockage_pions[col, row + 2]
                    == self.stockage_pions[col, row + 3]
                    == 'o'
                ):
                    return True

        # Vérification des colonnes verticales
        for col in range(rows - 3):
            for row in range(cols):
                if (
                    self.stockage_pions[5 - col, row] == self.stockage_pions[4 - col, row]
                    == self.stockage_pions[3 - col, row]
                    == self.stockage_pions[2 - col, row]
                    == 'x'
                    ):
                    return True
                if (
                    self.stockage_pions[5 - col, row] == self.stockage_pions[4 - col, row]
                    == self.stockage_pions[3 - col, row]
                    == self.stockage_pions[2 - col, row]
                    == 'o'
                    ):
                    return True

        # Vérification des diagonales descendantes
        for col in range(3, rows):
            for row in range(cols - 3):
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col - 1, row + 1]
                    == self.stockage_pions[col - 2, row + 2]
                    == self.stockage_pions[col - 3, row + 3]
                    == 'x'
                ):
                    return True
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col - 1, row + 1]
                    == self.stockage_pions[col - 2, row + 2]
                    == self.stockage_pions[col - 3, row + 3]
                    == 'o'
                ):
                    return True

        # Vérification des diagonales ascendantes
        for col in range(rows - 3):
            for row in range(cols - 3):
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col + 1 , row + 1]
                    == self.stockage_pions[col + 2, row + 2]
                    == self.stockage_pions[col + 3, row + 3]
                    == 'x'
                ):
                    return True
                if (
                    self.stockage_pions[col, row] == self.stockage_pions[col + 1 , row + 1]
                    == self.stockage_pions[col + 2, row + 2]
                    == self.stockage_pions[col + 3, row + 3]
                    == 'o'
                ):
                    return True
        return False


    def placer_un_pion(self, joueur, position):
        """Placer un pion.

        Pour le joueur spécifié, placer un pion à la position spécifiée.

        Args:
            joueur (int): Le numéro du joueur.
            position (int): La position du pion.
        
        Raises:
            Puissance4_Error: Si le numéro du joueur est autre que 1 ou 2.
            Puissance4_Error: Si la position est invalide.
            Puissance4_Error: Si la collone est pleine.
        """

        if joueur not in (1, 2):
            raise Puissance4_Error("Le numéro du joueur est autre que 1 ou 2.")


        #Vérifier si la position est valide
        if position < 1 or position > 7:
            raise Puissance4_Error("La position est invalide.")

        #Vérifier si la collone est pleine
        if self.stockage_pions[0, position - 1] != '.':
            raise Puissance4_Error("La collone est pleine.")

        for i in range(5, -1, -1):
            if self.stockage_pions[i, position - 1] == '.':
                pos = [position, 6 - i]
                break
        self.état['joueurs'][joueur - 1]['pions'].append(pos)
        self.actualiser()
        if self.joueur == 1:
            self.joueur = 2
        else:
            self.joueur = 1

    def actualiser(self):
        """Actualiser le damier.

        Mettre à jour le damier en fonction de l'état du jeu.
        """
        # Récupérer des tableaux "joueurs" et "murs"
        pion1 = self.état['joueurs'][0]['pions']
        pion2 = self.état['joueurs'][1]['pions']


        # Création des tableaux de données
        self.stockage_pions = Table(6,7,'.')

        #Indice de haut de tableau
        index = 6

        #Ajout des murs verticaux
        for pion in pion1:
            self.stockage_pions[index - pion[1], pion[0]-1] =  'o'
        for pion in pion2:
            self.stockage_pions[index - pion[1], pion[0]-1] =  'x'

    def formater_damier(self):
        """Formater le damier.

        Formater le damier pour l'affichage.

        Returns:
            str: Le damier formaté.
        """
        #Actualiser le damier
        self.actualiser()

        #Retourner le damier
        return make_grid(self.stockage_pions)


    def récupérer_le_coup(self, joueur):
        """Récupérer le coup.

        Demander au joueur spécifié de saisir un coup.

        Args:
            joueur (int): Le numéro du joueur.

        Returns:
            int: La position du pion.

        Raises:
            Puissance4_Error: Si le numéro du joueur est autre que 1 ou 2.
            Puissance4_Error: La collone sélectionnée est invalide.
        """
        if joueur not in (1, 2):
            raise Puissance4_Error("Le numéro du joueur est autre que 1 ou 2.")

        #Demande de position
        position = input("Entrez la collone du pion à poser: ")

        if position not in ('1', '2', '3', '4', '5', '6', '7'):
            raise Puissance4_Error("La collone sélectionnée est invalide.")

        position = int(position)

        return position

    def est_egalite(self):
        """Déterminer si la partie est nulle (égalité).

        Returns:
            bool: True si le jeu est nul (égalité); False sinon.
        """
        for value in self.stockage_pions.get_line(0):
            if value == '.':
                return False
        return True


    def __str__(self):
        """Retourner une représentation en chaîne de caractères du jeu.

        Returns:
            str: Une représentation en chaîne de caractères du jeu.
        """
        return self.formater_damier()

    def gestion_de_jeu(self, joueur):
        """Gestion de jeu.

        Gérer le jeu en fonction de l'état du jeu.
        Actualiser le score dans le tableau et afficher le gagnant.

        Args:
            x (int): Le numéro du joueur.
        """
        if self.est_egalite():
            self.tab[0] += 1
            print("    Égalité")
        else:
            self.tab[joueur%2 + 1] += 1
            print(f"    Le gagnant est {self.état['joueurs'][joueur%2]['nom']}")


    def restart(self):
        """Redémarrer le jeu.

        Demander au joueur s'il veut recommencer une partie.

        Returns:
            bool: True si le joueur veut recommencer; False sinon.
        """
        flag = input("Voulez-vous recommencer? (o/n): ")
        if flag == 'o':
            flag = True
        else:
            flag = False
        return flag




class Table:
    """Cette classe encapsule une table à deux dimensions en stockant
    ses rangées bout à bout dans une liste. Si la table possède m rangées
    et n colonnes, alors l'élément (i,j) de la table se trouve à l'indice
    i*n+j dans la liste."""

    def __init__(self, m_size, n_size, item):
        self.m_size = m_size
        self.n_size = n_size
        self.data =[]

        # Initialiser la liste avec les caractères
        self.set_values(item for _ in range(m_size*n_size))

    # Méthode pour récurérer une valeur dans la liste
    def __getitem__(self, index):
        i, j = index
        return self.data[i*self.n_size + j]

    # Méthode pour modifier une valeur dans la liste
    def __setitem__(self, index, x_value):
        i, j = index
        self.data[i*self.n_size + j] = x_value

    # Méthode pour modifier les valeurs de la liste
    def set_values(self, iterable):
        """Modifier les valeurs de la liste

        Args:
            iterable (iterable): Iterable contenant les valeurs

        Returns:
            Table: L'instance de la classe
        """
        data = list(iterable)
        self.data = data
        return self

    # Méthode pour récupérer les lignes des listes
    def get_line(self, i):
        """ Récupérer une ligne de la liste

        Args:
            i (int): Numéro de la ligne

        Returns:
            list: Une liste contenant les éléments de la ligne
    """
        return self.data[i*self.n_size:(i+1)*self.n_size]


    # Méthode pour récupérer les dimensions de la liste
    def get_size(self):
        """ Récupérer les dimensions de la liste

        Args:
            Aucun

        Returns:
            tuple: Un tuple contenant les dimensions de la liste
        """
        return self.m_size, self.n_size


# Créer la ligne supérieure du damier
def make_top_line():
    """Créer la ligne supérieure du damier

    Args:
        Aucun

    Returns:
        str: Une chaîne de caractères représentant la ligne supérieure du damier
    """
    return '   ---------------------------'


# Créer la ligne inférieure du damier
def make_bottom_line():
    """Créer la ligne inférieure du damier

    Args:
        Aucun

    Returns:
        str: Une chaîne de caractères représentant la ligne inférieure du damier
    """
    return '--|---------------------------\n  | 1   2   3   4   5   6   7'


# Créer une ligne du damier
def make_data_line(ligne_pion):
    """Créer une ligne du damier

    Args:
        ligne_joueur (list): Une liste contenant les valeurs de la ligne du tableau joueurs

    Returns:
        str: Une chaîne de caractères représentant une ligne du damier
    """
    # Initialiser une variable d'accumulation pour la ligne
    res = ''

    # Si aucune valeur, retourner une chaîne vide
    if len(ligne_pion) == 0:
        return res

    # Pour chaque élément de la ligne
    for j in ligne_pion[:-1]:

        # Ajouter les valeurs de chaque ligne des tableaux joueurs et murs
        res += f"{j}   "

    # Ajouter la dernière valeur de la ligne du tableau joueurs (car de taille n+1)
    return res + f"{ligne_pion[-1]}"


def make_grid(table_pions):
    """Créer le damier

    Args:
        
        table_joueurs (Table): Une instance de la classe Table représentant le tableau joueurs
    Returns:
        str: Une chaîne de caractères représentant le damier
    """
    # Déterminer les dimensions du tableau de réference murs
    m_size = table_pions.get_size()[0]

    # Initaliser une variable d'accumulation pour le résultat
    res = ''

    # Pour chaque ligne du tableau
    for i in range(m_size):

        # Si première ligne, ajouter une ligne de séparation
        if i == 0:
            res += make_top_line()+'\n'

        # Ajouter la ligne de données
        line = make_data_line(table_pions.get_line(i))
        res += f"{m_size-i} | " + line + ' |\n'

        # Si dernière ligne, ajouter une ligne de séparation
    res += make_bottom_line()+'\n'

    return res
