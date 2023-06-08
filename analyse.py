"""Module de fonctions utilitaires pour le jeu jeu Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
"""

import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                    Cet objet a deux attributs:  « graphique » qui est un booléen `True`/`False`
                    et « normal » qui est un booléen `True`/`False`.
    """
    # Créer un interpréteur de commande
    parser = argparse.ArgumentParser(description="Puissance 4")

    # Ajouter les arguments
    parser.add_argument('-g', '--graphique', action = 'store_true',
                        help = 'Activer le mode graphique.', default=False)
    parser.add_argument('-n', '--normal',  action = 'store_true',
                        help = 'Activer le mode normal.', default=False)

    return parser.parse_args()
