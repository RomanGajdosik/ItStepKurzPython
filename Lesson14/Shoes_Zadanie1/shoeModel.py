class ShoeModel:
    def __init__(self):
        self.shoes = []
    def add_shoe(self,shoe):
        self.shoes.append(shoe)
    def remove_shoe(self,id):
        self.shoes.remove(id)
    def show_all_shoes(self):
        return self.shoes
    def show_shoes_size(self,size):
        pass #!!dorobit
    def show_all_shoes_price(self):
        pass #!!dorobit
