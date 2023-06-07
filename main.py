from puissance4 import Puissance4
from puissance4x import Puissance4X
from analyse import analyser_commande  


if __name__ == "__main__":
    args = analyser_commande()
    if args.graphique:
        print("Mode graphique")
        flag = True
        jeu = Puissance4X(['Joueur 1', 'Joueur 2'])
        while flag:
            jeu = Puissance4X(['Joueur 1', 'Joueur 2'], jeu.tab)
            jeu.draw_grid()

            while not jeu.est_terminée() and not jeu.est_egalite():
                jeu.afficher()
                coup = jeu.attente_coup()
                jeu.placer_un_pion(jeu.joueur, coup)

            jeu.gestion_de_jeu(jeu.joueur)
            flag = jeu.restart()
            print("Partie terminée")

    elif args.normal:
        print("Mode normal")
        flag = True
        jeu = Puissance4(['Joueur 1', 'Joueur 2'])
        while flag:
            jeu = Puissance4(['Joueur 1', 'Joueur 2'], jeu.tab)

            while not jeu.est_terminée() and not jeu.est_egalite():
                print("Tour du joueur", jeu.joueur)
                print(jeu)
                coup = jeu.récupérer_le_coup(jeu.joueur)
                jeu.placer_un_pion(jeu.joueur, coup)
                print(jeu.stockage_pions[5,4])
            jeu.gestion_de_jeu(jeu.joueur)
            flag = jeu.restart()
            print("Partie terminée")

    print(f"\nScore : Joueur 1 : {jeu.tab[1]} / Joueur 2 : {jeu.tab[2]} / Égalité : {jeu.tab[0]}")