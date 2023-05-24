from perso import menu_option_perso
from jobs import menu_option_job
from supermarcher import menu_option_superm
from gestion_fichier import lecture, sauvegarde,retour_menu


menu_option=[{
    'indice':'1',
    'description':'gestion du perso',
    'fonction': menu_option_perso
},{
    'indice':'2',
    'description':'gestion jobs',
    'fonction': menu_option_job 
},{
    'indice':'3',
    'description':'Le marché',
    'fonction': menu_option_superm
}]

def menu_principal():
    g=True
    while True:
        for option in menu_option:
            print(f"[{option['indice']}] {option['description']}")
        
        print("[quit] QUITTEZ")
        print("Que veut tu faire ?")
        x=input("==>")
        if x=='quit' or x=='QUIT':
            g=False
            break
        for option in menu_option:
            if x == option['indice']:
                z=option['fonction']()
                
        if z != True:
            g=False
            break
        

menu_principal()


