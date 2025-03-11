from abc import ABC, abstractmethod

class Zviera(ABC):
    
    @abstractmethod
    def zvuk(self):
        pass
    @abstractmethod
    def jedlo(self):
        pass
class Macka(Zviera):
    def zvuk(self):
        print("Mňau")
    def jedlo(self):
        print('Kapsicky')
class Pes(Zviera):
    def zvuk(self):
        print('HAF HAF')
    def jedlo(self):
        print("granule")

macka = Macka()
pes = Pes()
#zviera = Zviera()
macka.zvuk()
macka.jedlo()
pes.jedlo()
pes.zvuk()
