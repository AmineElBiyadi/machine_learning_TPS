from Personne import Personne

class Etudiant(Personne):
    def __init__(self, id, name,prenom, age, filiere, niveau, **kwargs):
        super().__init__(id, name, prenom, age, **kwargs)
        self.filiere = filiere
        self.niveau = niveau
        self.list_notes = []

    def ajouterNotes(self,*notes):
        for note in notes: 
            self.list_notes.append(note)
    
    def afficherEtudiant(self):
        print(f"Les informations de l'etudiant numero {self.id} sont : \n\t Nom : {self.name} || Prenom : {self.prenom} || Age : {self.age} || Filiere : {self.filiere} || Niveau : {self.niveau} || Notes : {self.list_notes if len(self.list_notes) != 0 else 'Aucune note'} || Moyenne : {self.moyenne() if len(self.list_notes) != 0 else 0}")
        if len(self.kwargs) != 0 :
            print("Les informations supplementaires de l'etudiant sont : ")
            for key,value in self.kwargs.items():
                print(f"\t  - {key} : {value}")

    def moyenne(self): 
        if len(self.list_notes) == 0 :
            return 0 
        else : 
            return sum(self.list_notes)/len(self.list_notes)