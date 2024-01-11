def additionner_listes(n1, n2):
    # Remplir les listes avec des zéros à gauche si nécessaire pour les égaler en longueur
    diff = len(n1) - len(n2)
    if diff > 0:
        n2 = [0] * diff + n2
    else:
        n1 = [0] * abs(diff) + n1

    # Initialiser la liste résultante avec des zéros
    somme = [0] * (len(n1) + 1)

    # Parcourir les listes de droite à gauche et effectuer l'addition
    retenue = 0
    for i in range(len(n1) - 1, -1, -1):
        total = n1[i] + n2[i] + retenue
        somme[i + 1] = total % 10  # Le chiffre de la somme
        retenue = total // 10  # La retenue

    # Gérer la retenue finale
    somme[0] = retenue

    # Supprimer les zéros non significatifs à gauche
    while somme[0] == 0:
        somme = somme[1:]

    return somme
