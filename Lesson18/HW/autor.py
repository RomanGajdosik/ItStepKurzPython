class Autor():
    def __init__(self,id,meno,bio):
        self.id = id
        self.meno = meno
        self.bio = bio
    def __str__ (self):
        return f"\n Id Autora: {self.id} \n Autor: {self.meno} \n Bio: {self.bio}"