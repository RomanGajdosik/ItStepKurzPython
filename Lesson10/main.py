# import math
#
# class Shape:
#     def calculate_area(self):
#         raise NotImplementedError('Podtrieda musi implemmentovat tuto metodu ')
#
# class Rectangle(Shape):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def calculate_area(self):
#         return self.a*self.b
# class Circle(Shape):
#     def __init__(self,r):
#         self.r = r
#     def calculate_area(self):
#         return math.pi*self.r*self.r
# class Right_triangle(Shape):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def calculate_area(self):
#         return (self.a*self.b)/2

class Platba:
    def zaplat(self):
        raise NotImplementedError('Podtrieda musi implemmentovat tuto metodu ')

class KreditnaKarta(Platba):
    def zaplat(self,suma=50):
        self.suma = suma
        return(f'Zaplatil si kreditnou kartou {self.suma}')
class Paypal(Platba):
    def zaplat(self):
        return('Zaplatil si cez Paypal')
class Hotovost(Platba):
    def zaplat(self):
        return('Zaplatil si v hotovosti')

kreditka = KreditnaKarta()
payp = Paypal()
cash= Hotovost()
for platba in [kreditka,payp,cash]:
    print(platba.zaplat())



# rect = Rectangle(2,2)
# circ = Circle(4)
# Right_tr = Right_triangle(3,4)
# for shape in [rect,circ,Right_tr]:
#     print(shape.calculate_area())