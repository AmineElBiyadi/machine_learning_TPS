from EtudiantGI import EtudiantGI
from Etudiant import Etudiant

students = {}

# everything is done except the suplumentary information like the email and the ville 


def ajouter_etudiant():
    print("---------- Ajouter un etudiant ----------")
    id = int(input("Entrez l'ID de l'etudiant : "))
    if students.get(id) is not None:
        print("Un etudiant existe deja avec cet ID .")
        while students.get(id) is not None:
            id = int(input("Reentrez l'ID de l'etudiant : "))

    name = input("Entrez le nom de l'etudiant : ")
    prenom = input("Entrez le prenom de l'etudiant : ")
    age = int(input("Entrez l'age de l'etudiant : "))
    filiere = input("Entrez la filiere de l'etudiant (par defaut GI): ")
    niveau = input("Entrez le niveau de l'etudiant (par defaut GI2): ")

    if filiere.upper() == "GI" or filiere == "" :
        option = input("Entrez l'option de l'etudiant : ")
        if niveau == "":
            niveau = "GI2"
        etudiant = EtudiantGI(id, name ,prenom, age, niveau, option)
    else:
        if niveau == "":
            print("Le niveau est obligatoire si la filiere n'est pas GI !!.")
            while niveau == "":
                niveau = input("Reentrez le niveau de l'etudiant : ")

        etudiant = Etudiant(id, name ,prenom, age, filiere, niveau)

    students[id] = etudiant
    print("L'etudiant est ajoute avec succes.")

def ajouter_notes(): 
    notes= []
    print("---------- Ajouter des notes ----------")
    id = int(input("Entrez l'ID de l'etudiant : "))
    if students.get(id) is None:
        print("L'etudiant n'existe pas.")
        return
    note = 0 
    while (note != -1) : 
        note = int(input("Enrez la note de l'etudiant (pour arreter entrez -1) : "))
        if note != -1 and note in range(0,21): 
            notes.append(note)
        elif note != -1 and note not in range(0,21) :
            print("La note doit etre entre 0 et 20 !!")
        else :
            if len(notes) != 0 : 
                students[id].ajouterNotes(*notes)
                print("Les notes sont ajoutees avec succes.")
                notes.clear()
            else :
                print("Aucune note n'est ajoutee !!")

def afficher_etudiants():
    print("---------- Afficher tous les etudiants ----------")
    for etudiant in students.values():
        print("------------------------------------------------------------")
        etudiant.afficherEtudiant()
    print("------------------------------------------------------------")   

def calculer_moyenne_generale():
    if len(students) == 0 :
        return 0
    else :
        sum_moyennes = 0 
        for etudiant in students.values() :
            sum_moyennes += etudiant.moyenne()
        return sum_moyennes / len(students)

def calculer_meilleure_et_pire_moyenne():
    if len(students) == 0 :
        return 0
    else : 
        students_sorted = classer_etudiants_par_moyenne("1")
        return {"meilleure": students_sorted[0].moyenne(),"pire": students_sorted[len(students_sorted)-1].moyenne()}

def afficher_statistiques():
    print("---------- Afficher les statistiques ----------")
    if len(students) == 0 :
        print("Aucun etudiant n'est enregistre !!")
        return
    print(f" \t- Le nombre totale des etudiants est : {len(students)}")
    print(f" \t- La moyenne generale de tous les etudiants est : {calculer_moyenne_generale()}")
    meilleure_et_pire_moyenne = calculer_meilleure_et_pire_moyenne()
    print(f" \t- La meilleure moyenne est : {meilleure_et_pire_moyenne['meilleure']} ")
    print(f" \t- La pire moyenne est : {meilleure_et_pire_moyenne['pire']}")

def rechercher_etudiant():
    print("---------- Rechercher un etudiant ----------")
    print("Veuillez choisir le critere de recherche :  1. Par ID || 2. Par nom et prenom")
    choice = input("  Veuillez entrez votre choix : ")
    if choice not in ["1","2"] :
        print("Choix invalide !!")
        print("Veuillez reessayer !!")
        return  
    if choice == "1" :
        id = int(input("Veuillez entrez l'ID de l'etudiant : "))
        if students.get(id) is None :
            print("L'etudiant n'existe pas !!")
        else :
            print("L'etudiant est trouve !! voici ses informations : ")
            students[id].afficherEtudiant()
    else :
        name = input("Veuillez entrez le nom de l'etudiant : ")
        prenom = input("Veuillez entrez le prenom de l'etudiant : ")
        if name == "" or prenom == "" :
            print("Veuillez entrez le nom et le prenom de l'etudiant !!")
            return
        for etudiant in students.values() :
            if etudiant.name == name and etudiant.prenom == prenom :
                print("L'etudiant est trouve !! voici ses informations : ")
                etudiant.afficherEtudiant()
                return
        print("L'etudiant n'existe pas !!")

def classer_etudiants_par_moyenne(order ):
    if order == "1":
        students_sorted = sorted(students.values(), key =lambda etudiant: etudiant.moyenne() , reverse=True)
    else:
        students_sorted = sorted(students.values(), key =lambda etudiant: etudiant.moyenne() , reverse=False)
    return students_sorted

def classer_et_afficher_etudiants_par_moyenne():
    print("---------- Classer les etudiants par moyenne ----------")
    print ("Veuillez choisir le critere de classement :  1. Par ordre decroissant || 2. Par ordre croissant")
    choice = input("  Veuillez entrez votre choix : ")
    if choice not in ["1","2"] :
        print("Choix invalide !!")
        print("Veuillez reessayer !!")
        return
    if len(students) == 0 :
        print("Aucun etudiant existe !!")
        return
    students_sorted = classer_etudiants_par_moyenne(choice)
    for etudiant in students_sorted : 
        print("-------------------------------------------------")
        etudiant.afficherEtudiant()
    print("-------------------------------------------------")

def supprimer_etudiant():
    print("---------- Supprimer un etudiant ----------")
    id = int(input("Enter l'ID de l'etudiant a supprimer : "))
    if students.get(id) is None:
        print("L'etudiant n'existe pas.")
        return
    students.pop(id)
    print("L'etudiant est supprime avec succes.")

def main() : 
    quit = 0
    while quit == 0:
        print("\n\n=================================================")
        print("     1. Ajouter etudiant ")
        print("     2. Ajouter des notes")
        print("     3. Afficher tous les etudiants")
        print("     4. Rechercher un etudiant")
        print("     5. Afficher les statistiques")
        print("     6. Classer les etudiants par moyenne")
        print("     7. Supprimer un etudiant")
        print("     8. Quitter")
        print("=================================================")
        choice = input("    Veuillez entrez votre choix : ")
        match choice :
            case "1" :
                ajouter_etudiant()
            case "2" :
                ajouter_notes()
            case "3" :
                afficher_etudiants()
            case "4" :
                rechercher_etudiant()
            case "5" :
                afficher_statistiques()
            case "6" :
                classer_et_afficher_etudiants_par_moyenne()
            case "7" :
                supprimer_etudiant()
            case "8" :
                quit = 1
            case _ :
                print("Choix invalide !!")
                print("Veuillez reessayer !!")

main()