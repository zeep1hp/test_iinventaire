import json

def lecture(nom):
    with open(nom, 'r') as f:
        return json.load(f)

    
def sauvegarde(nom,variable):
    with open(nom, 'w') as f:
        json.dump(variable, f)

def retour_menu():
    liste_choix = ["oui","OUI","non","NON"]
    print("Veut tu retourner du menu ? (oui|non)")
    x=input("==>")
    while x not in liste_choix:
        print("Veut tu retourner du menu ? (oui|non)")
        x=input("==>")
    if x == "oui" or x == "OUI":
        return True
    else:
        return False