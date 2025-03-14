class Shoe():
    def __init__(self,id,gender_type,Type,color,price,brand,size):
        self.id = int(id)
        self.gender_type = gender_type
        self.type = Type
        self.color =color
        self.price = float(price)
        self.brand = brand
        self.size = size
    def __str__(self):
        return f"Shoe Id:{self.id} Type:{self.gender_type} type:{self.type} color: {self.color} price:{self.price} brand:{self.brand} size: {self.size}"