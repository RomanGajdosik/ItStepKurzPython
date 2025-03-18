class Calc:

    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
    def divide(self, a, b):
        return a/b
    def odvesna(self,c,a):
        return (c**2-a**2)**0.5
    def korene(self,a,b,c):
        return ((-b+(b**2-4*a*c)**0.5)/(2*a), (-b-(b**2-4*a*c)**0.5)/(2*a))