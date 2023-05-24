from gestion_fichier import lecture,sauvegarde,retour_menu
f_perso="perso.json"
f_jobs="job.json"
job = lecture(f_jobs)
perso = lecture(f_perso)

def print_job():
    for element in job:
        print(f"{element['nom']} est payer {element['salaire']}")

def affect_job():
    if perso['travail'] == "aucun":
        print_job()
        print("\nQuel métier souhaite tu faire ?")
        x=input("==>")
        for element in job:
            if x == element['nom']:
                perso['travail']=element['nom']
                sauvegarde(f_perso,perso)
                print(f"tu travaille maintenant en tant que {perso['travail']}")
    else:
        print(f"tu travail déja en tant que {perso['travail']}")

def quittez_job():
    liste_choix=["oui", "OUI","non","NON"]
    if perso['travail'] != "aucun":
        print(f"Veut tu réelement quittez ton travail actuel de {perso['travail']}?")
        x=input("==>")
        while x not in liste_choix:
            print(f"Veut tu réelement quittez ton travail actuel de {perso['travail']}?")
            x=input("==>")
        if x == "oui" or "OUI":
            perso['travail']="aucun"
            print("Vous avais bien quittez votre travail")
            sauvegarde(f_perso,perso)
    else:
        print("tu n'as pas de job debile vas en chercher un !")
    

def travailler():
    
    for element in job:
        
        if perso['travail']==element['nom'] and perso['stamina'] >= element['energie']:
            perso['wallet']+=element['salaire']
            perso['stamina']-=element['energie']
            print(f"tu a gagner {element['salaire']} aujourd'hui, il te reste {perso['stamina']} d'energie")
            sauvegarde(f_perso,perso)
            break
    else:
        print("tu ne remplis pas les conditions pour travailler")    


menu_job=[{
    'indice':'1',
    'description':'trouve un travaille',
    'fonction': affect_job
},{
    'indice':'2',
    'description':'démision d\'un travaille',
    'fonction': quittez_job
},{
    'indice':'3',
    'description':'Faire une journée de travail',
    'fonction': travailler
}]

def menu_option_job():
    for option in menu_job:
        print(f"[{option['indice']}]  {option['description']}")
    print("Que veut tu faire ?")
    x=input("==>")
    for option in menu_job:
        if x == option['indice']:
            option['fonction']()
    d=retour_menu()
    if d==True:
        return True
    else:
        return False

#menu_option_job()
#quittez_job()
#affect_job()
#travailler()