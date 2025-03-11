from shoe import Shoe

class ShoesControler():
    def __init__(self,model,view):
        self.model = model 
        self.view = view

    def add_shoe(self,id,gender_type,Type,color,price,brand,size):
        shoe = Shoe(id,gender_type,Type,color,price,brand,size)
        self.model.add_shoe(shoe)
    def display_shoes(self):
        shoes = self.model.show_all_shoes()
        self.view.display_shoes(shoes)