class Napoj:
    def cena(self):
        raise NotImplementedError

class Kava(Napoj):
    def cena(self):
        return 2

class Caj(Napoj):
    def cena(self):
        return 3

class PrisadaDecorator(Napoj):
    def __init__(self, napoj):
        self._napoj = napoj

    def cena(self):
        return self._napoj.cena()

class Mlieko(PrisadaDecorator):
    def cena(self):
        return self._napoj.cena() + 5

class Cukor(PrisadaDecorator):
    def cena(self):
        return self._napoj.cena() + 2

# Použitie Dekorátora
moja_kava = Kava()
moja_kava = Mlieko(moja_kava)
moja_kava = Cukor(moja_kava)
print(moja_kava.cena())

moj_caj = Caj()
moj_caj = Cukor(moj_caj)
print(moj_caj.cena())
