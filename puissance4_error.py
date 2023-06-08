"""Module pour les erreurs du jeu Puissance4.

Ce module contient la classe Puissance4 qui permet de gérer les erreurs du jeu Puissance4."""

class Puissance4_Error(Exception):
    """Classe d'erreur pour le jeu Puissance4.

    Attributes:
        message (str): Message d'erreur"""

    def __init__(self, message):
        """Constructeur de la classe Puissance4_Error.

        Args:
            message (str): Message d'erreur
        """
        self.message = message

    def __str__(self):
        """Méthode pour afficher le message d'erreur

        Returns:
            str: Message d'erreur
        """
        return self.message
    