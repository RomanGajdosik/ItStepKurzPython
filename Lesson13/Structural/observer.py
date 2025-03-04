class AkciovaBurza:
    def __init__(self):
        self._investori = []
        self._cena_akcie = None

    def pridaj_investora(self, investor):
        self._investori.append(investor)

    def odstran_investora(self, investor):
        self._investori.remove(investor)

    def notifikuj_investorov(self):
        for investor in self._investori:
            investor.update(self._cena_akcie)

    def set_cena_akcie(self, cena):
        self._cena_akcie = cena
        self.notifikuj_investorov()

class Investor:
    def update(self, cena):
        print(f"Aktualizovaná cena akcie: {cena}")

burza = AkciovaBurza()
investor1 = Investor()
investor2 = Investor()
investor3 = Investor()

burza.pridaj_investora(investor1)
burza.pridaj_investora(investor2)


burza.set_cena_akcie(100)
burza.set_cena_akcie(200)