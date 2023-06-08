"""Module de la classe Puissance4X

Classes:
    * Puissance4X - Classe pour afficher le jeu Puissance4.
"""
import turtle

from puissance4 import Puissance4

class Puissance4X(Puissance4):
    """Classe pour afficher le jeu Puissance4.

    Attributes:
        * fen (turtle.Screen) - Fenêtre de jeu.
        * damier (turtle.Turtle) - Dessine le damier.
        * maj (turtle.Turtle) - Affiche les mises à jour.
        * coup (list) - Coup à jouer.
        * jeu (int) - Etat de jeu (En cours : 1 sinon 0).

    """
    def __init__(self, joueur, tab=None):
        """Constructeur de la classe Puissance4X.

        Création des instances de turtle pour l'affichage du jeu.

        Args:
            * joueur (list) - Liste des joueurs.
            * tab (list) - Tableau de jeu.
        """
        super().__init__(joueur, tab)
        self.joueur = 1
        self.coup = None
        self.jeu = 1
        self.fen = turtle.Screen()
        self.fen.bgcolor("#e4d5b7")
        self.fen.tracer(False)
        self.fen.setup(1200, 700)
        self.fen.onclick(self.recup_pion, btn=1)
        self.damier = turtle.Turtle()
        self.maj = turtle.Turtle()
        self.maj.hideturtle()
        self.damier.hideturtle()

    def draw_grid(self):
        """Dessine une grille 6x7."""
        self.damier.speed(0)
        self.damier.hideturtle()
        self.damier.penup()
        self.damier.pensize(5)

        self.damier.color('white')
        for i in range(1, 7):
            self.damier.goto(-262.5 + i * 75, 225)
            self.damier.pendown()
            self.damier.goto(-262.5 + i * 75, -225)
            self.damier.penup()
        for i in range(1, 7):
            self.damier.goto(-262.5, -225 + i * 75)
            self.damier.pendown()
            self.damier.goto(262.5, -225 + i * 75)
            self.damier.penup()

        self.damier.color('black')
        self.damier.goto(-262.5, 225)
        self.damier.pendown()
        self.damier.goto(-262.5, -225)
        self.damier.penup()
        self.damier.goto(-262.5, -225)
        self.damier.pendown()
        self.damier.goto(262.5, -225 )
        self.damier.penup()
        self.damier.goto(-262.5, 225)
        self.damier.pendown()
        self.damier.goto(262.5, 225)
        self.damier.penup()
        self.damier.goto(262.5, -225)
        self.damier.pendown()
        self.damier.goto(262.5, 225)
        self.damier.penup()


    def recup_pion(self, pos_x, pos_y):
        '''Récupère le pion sur lequel on a cliqué
        et le stocke dans self.coup

        Args:
            pos_x (int) - Position x du clic.
            pos_y (int) - Position y du clic.
        '''
        if self.jeu == 1:
            self.fen.onclick(None, btn=1)
            self.coup = int((pos_x / 75 + 0.5) // 1 + 4)
            self.fen.onclick(self.recup_pion, btn=1)
            self.fen.update()
        else:
            self.fen.onclick(None, btn=1)
            self.coup = pos_x, pos_y
            self.fen.onclick(self.recup_pion, btn=1)
            self.fen.update()



    def afficher_pion(self, position, joueur):
        '''Affiche un pion en couleur sur le damier.

        Args:
            position (list) - Position du pion.
            color (str) - Couleur du pion.
        '''
        self.maj.penup()
        self.maj.goto((position[0] - 4) * 75, (position[1] - 3.5) * 75)
        if joueur == 1:
            color = 'yellow'
        else:
            color = 'red'
        self.maj.dot(50, color)
        self.fen.update()

    def afficher(self):
        '''Affiche le jeu dans la fenêtre turtle.

        Affiche les pions des joueurs et la légende du jeu.
        '''
        self.coup = None
        self.maj.clear()
        pions_j1 = self.état['joueurs'][0]['pions']
        pions_j2 = self.état['joueurs'][1]['pions']
        for pion in pions_j1:
            self.afficher_pion(pion, 1)
        for pion in pions_j2:
            self.afficher_pion(pion, 2)
        if self.jeu:
            self.formater_légende_graphique()
            self.afficher_victoire()


    def formater_légende_graphique(self):
        '''Affiche la légende du jeu dans la fenêtre turtle.

        Affiche le nom du joueur qui doit jouer.
        '''
        self.maj.penup()
        self.maj.goto(-160.0, -285.0)
        self.maj.pendown()
        if self.joueur == 1:
            légende = f"Au tour de {self.état['joueurs'][0]['nom']} de jouer"
            self.maj.color('yellow')
        else:
            légende = f"Au tour de {self.état['joueurs'][1]['nom']} de jouer"
            self.maj.color('red')
        self.maj.write(légende, font=("Arial", 20, "normal"))
        self.maj.penup()
        self.fen.update()

    def afficher_victoire(self):
        '''Affiche le nombre de victoires de chaque joueur dans la fenêtre turtle.

        Affiche le nombre de victoires de chaque joueur et le nombre d'égalités.
        '''
        self.maj.penup()
        self.maj.goto(-520, 150)
        self.maj.pendown()
        self.maj.color('yellow')
        self.maj.write(f"Victoire J1 : {self.tab[1]}", font=("Arial", 25, "normal"))


        self.maj.penup()
        self.maj.goto(-520, 75)
        self.maj.pendown()
        self.maj.color('red')
        self.maj.write(f"Victoire J2 : {self.tab[2]}", font=("Arial", 25, "normal"))


        self.maj.penup()
        self.maj.goto(-520, 0)
        self.maj.pendown()
        self.maj.color('black')
        self.maj.write(f"Egalité : {self.tab[0]}", font=("Arial", 25, "normal"))



    def attente_coup(self):
        '''Attend que le joueur joue un coup.

        Returns:
            coup (int) - Coup joué par le joueur.
        '''
        while not self.coup:
            self.fen.update()
        return self.coup

    def écrire(self, mot, pos_x, pos_y, mot_x, mot_y, color):
        '''Ecrit un mot dans un rectangle.

        Args:
            mot (str) - Mot à écrire.
            a (int) - Position x du coin supérieur gauche du rectangle.
            b (int) - Position y du coin supérieur gauche du rectangle.
            c (int) - Position x du centre du mot.
            d (int) - Position y du centre du mot.
            color (str) - Couleur du rectangle.
        '''
        largeur_rectangle = 200
        hauteur_rectangle = 100
        self.maj.penup()
        self.maj.goto(pos_x, pos_y)
        self.maj.pendown()
        self.maj.pensize(5)
        self.maj.color(color)
        for _ in range(2):
            self.maj.forward(largeur_rectangle)
            self.maj.left(90)
            self.maj.forward(hauteur_rectangle)
            self.maj.left(90)
        self.maj.penup()
        self.maj.goto(mot_x, mot_y)
        self.maj.color(color)
        self.maj.write(mot, align="center", font=("Arial", 20, "normal"))
        self.maj.penup()
        self.fen.update()


    def restart(self):
        '''Redémarre la partie.

        Propose un affichage pour redémarrer la partie ou quitter le jeu.

        Returns:
            True si le joueur veut redémarrer la partie.
            False sinon.
        '''
        self.damier.clear()
        self.maj.clear()
        self.jeu = 0
        self.écrire('Restart', -350, 100, -250, 135, 'green')
        self.écrire('Quit', 110, 100, 210, 135, 'red')
        self.coup = None
        while self.jeu == 0:
            self.attente_coup()
            if (self.coup[0] > -350 and self.coup[0] < -150 and
                self.coup[1] > 100 and self.coup[1] < 200):
                self.jeu = 1
                self.fen.clear()
                return True

            elif (self.coup[0] > 110 and self.coup[0] < 310 and
                  self.coup[1] > 100 and self.coup[1] < 200):
                self.jeu = 1
                self.fen.bye()
                return False

            else:
                self.coup = None
