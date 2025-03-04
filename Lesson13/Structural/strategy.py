def ziadna_zlava(cena):
    return cena

def percentualna_zlava(cena):
    return cena * 0.90

def pevna_zlava(cena):
    return cena - 100 if cena > 100 else cena

class NakupnyKosik:
    def __init__(self, cena, strategia_zlavy=ziadna_zlava):
        self.cena = cena
        self.strategia_zlavy = strategia_zlavy

    def nastav_strategiu(self, nova_strategia):
        self.strategia_zlavy = nova_strategia

    def vypocitaj_cenu(self):
        return self.strategia_zlavy(self.cena)

kosik = NakupnyKosik(500)
print(f"Pôvodná cena: {kosik.cena}")
print(f"Cena po zľave: {kosik.vypocitaj_cenu()}")

kosik.nastav_strategiu(percentualna_zlava)
print(f"Cena po percentuálnej zľave: {kosik.vypocitaj_cenu()}")

kosik.nastav_strategiu(pevna_zlava)
print(f"Cena po pevnej zľave: {kosik.vypocitaj_cenu()}")

