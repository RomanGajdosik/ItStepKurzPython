import pickle
class Student():
    def __init__(self,name,age,country):
        self.name = name
        self.age  = age
        self.country = country
    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age} rokov"

patrik = Student("Patrik","30","Slovakia")
bytes_patrik = pickle.dumps(patrik)
print(patrik)
print(bytes_patrik)
patrik_nove=pickle.loads(bytes_patrik)
print(patrik_nove)
print(patrik == patrik_nove) # po naloadovani z bytestreamu sa identicky objekt ulozi do novej adresy v pameti takze niej identicky 
with open ('patrik.pickle','wb') as filehandler:
        pickle.dump (patrik,filehandler)
with open('patrik.pickle','rb') as filehandler:
     patrik_novy = pickle.load(filehandler)
     print('TOTO JE PRIDANE :\n',patrik_novy)