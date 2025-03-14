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
        shoes_size =[]
        for searched_shoe in self.shoes:
            if searched_shoe.size == size:
                shoes_size.append(searched_shoe)
        return shoes_size
    def show_shoes_overall_price(self):
        total_price = 0.00
        for shoe in self.shoes:
            total_price += float(shoe.price)
        return total_price

    def find_shoe(self,shoe):
        isThere = False
        for shoe_toFind in self.shoes:
            if shoe_toFind.id == shoe.id and shoe_toFind.gender_type == shoe.gender_type and shoe_toFind.type == shoe.type and shoe_toFind.color == shoe.color and shoe_toFind.price == shoe.price and shoe_toFind.brand == shoe.brand and shoe_toFind.size == shoe.size:
                isThere = True
        return isThere