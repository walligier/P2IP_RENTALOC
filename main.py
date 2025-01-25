#%%Import

import numpy as np
import pandas as pd
from datetime import datetime

#%% Creation des DataFrame de Données

DataClient = pd.DataFrame(columns = ["IDClient", "Emplacement", "Loyermax", "Surfacemin", "Colocation","DateEntré","DateFin", "DPEmin" ])

DataLogement = pd.DataFrame(columns=["IDLogement","Emplacement", "Loyer", "Surface", "Colocation","DateDebut", "DateFin", "DPE" ])

DataAgence = pd.DataFrame(columns = ["IDAgence","Emplacement"])

#%% Matching des données

def MatchingClient(client):
    """Algorythme qui a partir des criteres d'un client cherchant un logement renvoie tous les logement
    verifiant ces criteres"""

    Logement_valide = []

    for i in range(len(DataLogement)):
        Idlogement = DataLogement.loc[i]["IDLogement"]
        if (client["Emplacement"] == DataLogement.loc[i]["Emplacement"] and
                client["Loyermax"] >= DataLogement.loc[i]["Loyer"] and
                client["Surfacemin"] <= DataLogement.loc[i]["Surface"] and
                client["Colocation"] == DataLogement.loc[i]["Colocation"] and
                client["DateEntré"] >= DataLogement.loc[i]["DateDebut"] and client["DateFin"] <= DataLogement.loc[i][
                    "DateFin"] and
                client["DPEmin"] >= DataLogement.loc[i]["DPE"]
        ):
            Logement_valide.append(Idlogement)

    return Logement_valide

#%%TEST
#Ajout d'un client et d'un logement
DataClient.loc[0] = [1, "Ternes", 800, 14, False, datetime(datetime.today().year,1,26), datetime(datetime.today().year, 1, 28), "C"]
DataLogement.loc[0] = [1103, "Ternes", 650, 15, False, datetime.now(), datetime(datetime.today().year, 1, 30), "B"]

#Test pour chaque client si un des logements correspond aux criteres

resultats = DataClient.apply(MatchingClient, axis=1)
print(resultats)