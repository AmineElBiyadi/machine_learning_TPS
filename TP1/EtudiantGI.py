from Etudiant import Etudiant


class EtudiantGI(Etudiant):
    def __init__(self, id, name,prenom, age, niveau):
        super().__init__(id, name, prenom, age, 'GI', niveau)