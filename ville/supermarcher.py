from gestion_fichier import lecture, sauvegarde,retour_menu

f_perso = "perso.json"
f_superm = "supermarcher.json"

perso= lecture(f_perso)
supermarcher=lecture(f_superm)



def afficher_produit_dispo():
    for objet in supermarcher['items']:
        if objet['nb'] != 0:
            print(f"il reste {objet['nb']} {objet['nom']} au prix de {objet['prix']}")


def acheter_un_item():
    print(f"tu as actuellement {perso['wallet']} pièces")
    afficher_produit_dispo()
    print("Que veut tu acheter ?")
    x=input("==>")
    for objet in supermarcher['items']:
        if objet['nb'] != 0 and perso['wallet'] >0:
            if x==objet['nom']:
                perso['wallet']-=objet['prix']
                for i in perso['inventaire']:
                    if i['name']== objet['nom']:
                        i['nombre']+=1
                        objet['nb'] -=1
                        sauvegarde(f_perso,perso)
                        sauvegarde(f_superm,supermarcher)
                        print(f"tu a bien achetez un(e) {objet['nom']}")


def vendre_un_item():
    for objet in perso['inventaire']:
        if objet['nombre']>0:
            print(f"tu as {objet['nombre']} {objet['name']}")

    print("Que veut tu vendre ?")
    x=input("==>")
    for objet in perso['inventaire']:    
        for item in supermarcher['items']:
            if objet['nombre']>0:
                if x==objet['name'] and x==item['nom']:
                    objet['nombre']-=1
                    item['nb']+=1
                    perso['wallet']+=round(item['prix'] *0.8)
                    print(f"tu as bien vendu {objet['name']} au prix de {round(item['prix']*0.8)}\ntu a maitenant {perso['wallet']} pieces")
                    sauvegarde(f_perso,perso)
                    sauvegarde(f_superm,supermarcher)


menu_superm = [{
    'indice':'1',
    'description':'affiche les produits dispo',
    'fonction': afficher_produit_dispo
},{
    'indice':'2',
    'description':'acheter des produits',
    'fonction': acheter_un_item
},{
    'indice':'3',
    'description':'vendre des produits',
    'fonction': vendre_un_item
}]

def menu_option_superm():
    for option in menu_superm:
        print(f"[{option['indice']}]  {option['description']}")
    
    print("Que veut tu faire ?")
    x=input("==>")
    for option in menu_superm:
        if x==option['indice']:
            option['fonction']()
    d=retour_menu()
    if d==True:
        return True
    else:
        return False

#menu_option_superm()
#acheter_un_item()