
def calcul_epargne_familles(comptes):
    epargne_par_famille = {}

    for compte in comptes:
        nom_famille = compte.get('nom')
        montant_epargne = compte.get('epargne', 0)

        if nom_famille not in epargne_par_famille:
            epargne_par_famille[nom_famille] = 0

        epargne_par_famille[nom_famille] += montant_epargne

    famille_epargne_min = min(epargne_par_famille, key=epargne_par_famille.get)
    famille_epargne_max = max(epargne_par_famille, key=epargne_par_famille.get)

    epargne_min = epargne_par_famille[famille_epargne_min]
    epargne_max = epargne_par_famille[famille_epargne_max]

    return famille_epargne_min, famille_epargne_max, epargne_min, epargne_max
comptes = [
    {'nom': 'Boismoneau', 'prenom': 'stephane', 'epargne': 2500},
    {'nom': 'Jambon', 'prenom': 'fred', 'epargne': 5000},
    {'nom': 'Durois', 'prenom': 'nicolas', 'epargne': 10000},
    {'nom': 'Gueux', 'prenom': 'phillipe', 'epargne': 1250},
    {'nom': 'Duchan', 'prenom': 'alice', 'epargne': 4530},
    {'nom': 'Lepenou', 'prenom': 'amed', 'epargne': 2200},
    {'nom': 'Gueux', 'prenom': 'bernard'},
    {'nom': 'Jambon', 'prenom': 'steven', 'epargne': 1670},
    {'nom': 'Gueux', 'prenom': 'sylvie', 'epargne': 3},
    {'nom': 'Durois', 'prenom': 'berbard', 'epargne': 300000},
]

famille_epargne_min, famille_epargne_max, epargne_min, epargne_max = calcul_epargne_familles(comptes)
print("Famille avec l'épargne minimale :", famille_epargne_min, "| Montant d'épargne :", epargne_min)
print("Famille avec l'épargne maximale :", famille_epargne_max, "| Montant d'épargne :", epargne_max)

