class JeuDeCartes:
    def __init__(self):
        self.cartes = [(v, c) for v in range(2, 15) for c in range(4)]

    def nom_carte(self, carte):
        valeurs = {2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept", 8: "Huit", 9: "Neuf", 10: "Dix",
                   11: "Valet", 12: "Dame", 13: "Roi", 14: "As"}
        couleurs = {0: "Pique", 1: "Trèfle", 2: "Carreau", 3: "Cœur"}
        valeur = valeurs[carte[0]]
        couleur = couleurs[carte[1]]
        return f"{valeur} de {couleur}"

    def battre(self):
        import random
        random.shuffle(self.cartes)

    def tirer(self):
        if len(self.cartes) > 0:
            return self.cartes.pop(0)
        else:
            return None
jeu = JeuDeCartes()
jeu.battre()
for n in range(53):
    c = jeu.tirer()
if c == None:
    print('Terminé !')
else:
    print(jeu.nom_carte(c))
