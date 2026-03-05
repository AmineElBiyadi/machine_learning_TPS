class Personne:
    def __init__(self,id, name,prenom, age , **kwargs):
        self.id = id
        self.name = name
        self.prenom = prenom
        self.age = age
        self.kwargs = kwargs
