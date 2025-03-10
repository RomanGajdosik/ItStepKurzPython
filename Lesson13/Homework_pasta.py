class Pasta:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)
    
    def __str__(self):
        return f"Meal is : {self.ingredients[0]} with {self.ingredients[1]} and {self.ingredients[2]} and {self.ingredients[3]}"

class Pasta_Builder:
    def __init__(self):
        self.pasta = Pasta()
    
    def type_of_pasta(self, pasta_type):
        self.pasta.add_ingredients(pasta_type)
        return self
    
    def type_of_sauce(self, sauce):
        self.pasta.add_ingredients(sauce)
        return self
    
    def type_of_topping(self, topping):
        self.pasta.add_ingredients(topping)
        return self
    
    def type_of_dressing(self, dressing):
        self.pasta.add_ingredients(dressing)
        return self
    
    def cook(self):
        return self.pasta

pasta1 = Pasta_Builder().type_of_pasta("Spaghetti").type_of_sauce("Tomato").type_of_topping("Cheese").type_of_dressing("Olive oil").cook()
print(pasta1)
pasta2 = Pasta_Builder().type_of_pasta("Penne").type_of_sauce("Alfredo").type_of_topping("Bacon").type_of_dressing("Pesto").cook()
print(pasta2)
pasta3 = Pasta_Builder().type_of_pasta("Fettuccine").type_of_sauce("Carbonara").type_of_topping("Mushrooms").type_of_dressing("Garlic").cook()
print(pasta3)