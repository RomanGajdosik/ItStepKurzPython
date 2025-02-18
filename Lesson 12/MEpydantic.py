import pickle
from pydantic import BaseModel


class Student(BaseModel):
    name : str
    age : int
    email : str

patrik = Student(name='Patrik',age=20,email='email@email.com')
print(patrik.model_dump_json()) 

# zadanie  # 
data = input('Zadaj data ')
for_sort = data.rsplit(',')
data = list()
for num in for_sort:
    data.append(int(num))

print(data)
with open ('zadanie','wb') as filehandler:
    pickle.dump(data,filehandler)
with open('zadanie','rb') as filehandler:
    novyList = pickle.load(filehandler)
    print(type(novyList))
    print(novyList)
    