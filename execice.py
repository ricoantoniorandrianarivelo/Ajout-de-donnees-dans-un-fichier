import json


def CalculHT(dic: dict):
    som1 = 0
    for el in donnees["articles"]:
        som1 = som1 + (el["prix_unitaire_ht"]* el["quantite"])
    return som1
    
def CalculTVA(dic: dict):
    som1 = 0
    for el in donnees["articles"]:
        som1 = som1 + (el["taux_tva"]* el["quantite"])
    return som1
    
def CalculTTC(dic: dict):
    som1 = 0
    for el in donnees["articles"]:
        som1 = som1 + (el["prix_total_ttc"]* el["quantite"])
    return som1
    
with open("recu.json", 'r') as f:
    donnees = json.load(f)
    print(type(donnees))
    
vaovao = {
      "montant_total_ht":  CalculHT(donnees),
      "montant_tva": CalculTVA(donnees),
      "montant_total_ttc": CalculTTC(donnees)
}

donnees.update(vaovao) 

print(donnees)

with open("recu.json", 'w') as f:
    json.dump(donnees, f, indent=4)
    
    

    