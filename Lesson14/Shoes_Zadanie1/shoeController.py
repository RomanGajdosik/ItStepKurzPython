from shoe import Shoe

class ShoesControler():
    def __init__(self,model,view):
        self.model = model 
        self.view = view

    def add_shoe(self,id,gender_type,Type,color,price,brand,size):
        shoe = Shoe(id,gender_type,Type,color,price,brand,size)
        if self.model.find_shoe(shoe):
            self.view.problem("allready in the database",shoe)
        elif shoe.price <= 0:
            self.view.problem('Price of cannot be 0',shoe)
        else:
            self.model.add_shoe(shoe)
    def remove_shoe(self,id):
        self.model.remove_shoes(id)
    def display_shoes(self):
        shoes = self.model.show_all_shoes()
        self.view.display_shoes(shoes)
    def display_Shoes_of_size(self,size):
        shoes_one_size = self.model.show_shoes_size(size)
        if len(shoes_one_size) == 0:
            print ('No shoes of this size in DB')
        else:
            self.view.display_shoes(shoes_one_size)
    def total_price(self):
        price = self.model.show_shoes_overall_price()
        self.view.display_price(price)