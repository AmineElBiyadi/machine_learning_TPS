from Etudiant import Etudiant


class EtudiantGI(Etudiant):
    def __init__(self, id, name,prenom, age, niveau , option):
        super().__init__(id, name, prenom, age, 'GI', niveau)
        self.option = option

    def afficherEtudiant(self):
        print(f"Les informations de l'etudiant numero {self.id} sont : \n\t Nom : {self.name} || Prenom : {self.prenom} || Age : {self.age} || Filiere : {self.filiere} || Niveau : {self.niveau} || Notes : {self.list_notes if len(self.list_notes) != 0 else 'Aucune note'} || Moyenne : {self.moyenne() if len(self.list_notes) != 0 else 0}")
    