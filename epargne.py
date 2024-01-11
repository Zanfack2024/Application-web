comptes = [
    {'nom': 'Boismoneau', 'prenom': 'stephane', 'epargne': 2500},
    {'nom': 'Jambon', 'prenom': 'fred', 'epargne': 5000},
    {'nom': 'Durois', 'prenom': 'nicolas', 'epargne': 10000},
    {'nom': 'Gueux', 'prenom': 'phillipe', 'epargne': 1250},
    {'nom': 'Duhan', 'prenom': 'alice', 'epargne': 4530},
    {'nom': 'Lepenou', 'prenom': 'amed', 'epargne': 2200},
    {'nom': 'Gueux', 'prenom': 'bernard'},
    {'nom': 'Jambon', 'prenom': 'steven', 'epargne': 1670},
    {'nom': 'Gueux', 'prenom': 'sylvie', 'epargne': 3},
    {'nom': 'durois', 'prenom': 'berbard', 'epargne': 300000}
]

# Initialisation des dictionnaires pour stocker l'épargne par famille
epargne_par_famille = {}

# Calcul de l'épargne par famille
for compte in comptes:
    nom_famille = compte['nom'].capitalize()  # Convertir le nom en majuscules pour uniformiser
    if 'epargne' in compte:
        epargne = compte['epargne']
    else:
        epargne = 0

    if nom_famille in epargne_par_famille:
        epargne_par_famille[nom_famille] += epargne
    else:
        epargne_par_famille[nom_famille] = epargne

# Trouver la famille avec la plus faible et la plus forte épargne
famille_min_epargne = min(epargne_par_famille, key=epargne_par_famille.get)
famille_max_epargne = max(epargne_par_famille, key=epargne_par_famille.get)
