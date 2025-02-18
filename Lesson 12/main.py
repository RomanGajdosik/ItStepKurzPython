class Student():
    def __init__(self,name,age,country):
        self.name = name
        self.age  = age
        self.country = country
    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"

patrik = Student("Patrik","30","Slovakia")
print(patrik)