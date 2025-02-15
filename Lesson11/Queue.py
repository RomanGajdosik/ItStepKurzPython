class Queue:
    def __init__(self):
        self.data = []

    def pridaj(self,data):
        self.data.append(data)

    def odober(self):
        if self.je_prazdna():
            return None
        return self.data.pop(0)

    def je_prazdna(self):

        return len(self.data) == 0


    def zobraz(self):
        return self.data



    # def menu(self):
    #     self.volba_Funkcie = input('Zadaj jednu z moznosti \n  1. Je prazdna \n 2.Je plna \n 3.Pridaj element \n 4.Vymaz element \n 5.Zobraz queue')


q = Queue()
q.pridaj(1)
q.pridaj(2)
q.pridaj(3)
print(q.je_prazdna())
print(q.zobraz())
