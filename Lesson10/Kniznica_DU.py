class kniha:
    def __init__(self,nazov,autor,ISBN,rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = True
        self.rok_vydania = rok_vydania

    def vypozicat (self):
        if (self.dostupna):
            self.dostupna = False
            print(f'Prave ste si pozicali knihu {self.nazov}')
        else:
            print('Ospravedlnujeme sa ale Kniha je prave pozicana.')
    def vratit(self):
        if (self.dostupna != True):
            self.dostupna = True
            print(f'Dakujeme za vratenie knihy {self.nazov} ')
        else:
            print('Kniha je dostupna na zapozicanie')
    def __str__(self):
        return f"Nazov: {self.nazov} -Autor: {self.autor} -Rok vyd.: {self.rok_vydania} -ISBN: {self.ISBN} - {'Dostupna' if self.dostupna else 'Vypozicana'} "

class kniznica():
    def __init__(self):
        self.zoznam_knih =[]

    def pridaj_knihu(self,kniha):
        self.zoznam_knih.append(kniha)

    def vyhladaj_knihu(self,nazov):
        vysledky = [kniha for kniha in self.zoznam_knih if nazov.lower() in kniha.nazov.lower() ]
        if vysledky:
            for kniha in vysledky:
                print(kniha)
        else:
           print(f'Ziadne knihy s nazvom obsahujucim ({nazov}) sa nenasli')
    def vypozicaj_knihu(self,isbn):
        for kniha in self.zoznam_knih:
            if kniha.ISBN == isbn:
                kniha.vypozicat()
                return
        print(f"Je mi luto ale kniha s ISBN {isbn} nebola najdena")
    def vrat_knihu(self,isbn):
        for kniha in self.zoznam_knih:
            if kniha.ISBN == isbn:
                kniha.vratit()
                return
        print(f"Je mi luto ale kniha s ISBN {isbn} nebola najdena")
    def zoznam_dostupnych_knih(self):
        dostupne = [kniha for kniha in self.zoznam_knih if kniha.dostupna]
        if dostupne:
            for kniha in dostupne:
                print(kniha)
        else:
            print('Lutujeme ale kniznica je prazdna')







Kniha0 = kniha('R.U.R','Karel Capek',9788027713684,2023)
Kniha1 = kniha("Tajomstvá vesmíru", "Ján Novák", 978-80-123456-7-8, 2020)
Kniha2 = kniha("Cesty poznania", "Martina Kováčová", 978-80-876543-2-1, 2018)
Kniha3 = kniha("Programovanie pre začiatočníkov", "Peter Horváth", 978-80-567890-1-2, 2021)
Kniha4 = kniha("Historické záhady", "Anna Bieliková", 978-80-345678-9-0, 2019)
Kniznica = kniznica()
Kniznica.pridaj_knihu(Kniha0)
Kniznica.pridaj_knihu(Kniha1)
Kniznica.pridaj_knihu(Kniha2)
Kniznica.pridaj_knihu(Kniha3)
Kniznica.pridaj_knihu(Kniha4)
Kniznica.vypozicaj_knihu(978-80-876543-2-1)
Kniznica.zoznam_dostupnych_knih()
Kniznica.vyhladaj_knihu('Cesty')
