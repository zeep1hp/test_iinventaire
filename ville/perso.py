from gestion_fichier import lecture,sauvegarde,retour_menu

f_perso="perso.json"
f_jobs="job.json"



jobs=lecture(f_jobs)
perso= lecture(f_perso)


def create_perso():
    
    perso['nom']=input("Nom de perso:\n==>")
    #perso['age']=input("Age du perso:\n==>")
    sauvegarde(f_perso,perso)

def print_travail():
    print(f"tu travail en tant que : {perso['travail']}")


def print_ci():
    print(f"nom :{perso['nom']}")
    print(f"age :{perso['age']}")




def print_inventaire():
    for objet in perso['inventaire']:
        if objet['nombre'] != 0:
            print((f"tu as {objet['nombre']} {objet['name']}"))


def print_wallet():
    print(f"tu as {perso['wallet']} pièces")


def print_stamina():
    print(f"tu as {perso['stamina']} points d'endurance")


def dormir():
    if perso['stamina'] != 100:
        perso['stamina'] += 70
        if perso['stamina'] >100:
            perso['stamina']=100

    print(f"tu viens de tte reposer tu a maintenant {perso['stamina']} point d'endurance")
    sauvegarde(f_perso,perso)   


menu_perso =[{
    'indice':'1',
    'description':'modifie ton nom',
    'fonction': create_perso
},{
    'indice':'2',
    'description':'affice ton metier',
    'fonction': print_travail
},{
    'indice':'3',
    'description':'affiche ta carte d\'identité',
    'fonction': print_ci
},{
    'indice':'4',
    'description':'affiche ton invetaire',
    'fonction': print_inventaire
},{
    'indice':'5',
    'description':'affiche ton porte-monaie',
    'fonction': print_wallet
},{
    'indice':'6',
    'description':'affiche ton endurace',
    'fonction': print_stamina
},{
    'indice':'7',
    'description':'Dormir pour recup ton endurance',
    'fonction': dormir
}]

def menu_option_perso():
    for option in menu_perso:
        print(f"[{option['indice']}]  {option['description']}")
    print("Que veut tu faire ?")
    x=input("==>")
    for option in menu_perso:
        if x==option['indice']:
            option['fonction']()
    d=retour_menu()
    if d==True:
        return True
    else:
        return False

#menu_option_perso()
#create_perso()
#dormir()
