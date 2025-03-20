class checker():
    @staticmethod
    def check(rod_cislo):
        if len(rod_cislo) > 10:
            return False
        elif not rod_cislo.isdigit():
            return False
        elif int(rod_cislo[2]) == 5 or int(rod_cislo[2]) == 6:
            if int(rod_cislo[2:4]) > 62 or int(rod_cislo[4:6]) == 00 or int(rod_cislo[4:6]) > 32 or int(rod_cislo[4:6] == 00):
                return False
            return "Zenske rodne cislo"
        
        #!! neplatne rodne cislo
        elif len(rod_cislo) == 9:
            if int(rod_cislo[0:2]) > 53:
                return False
            elif rod_cislo[2:4] >= "13" or rod_cislo[2:4] == "00" or rod_cislo[4:6] >= "32" or rod_cislo[4:6] == "00":
                return False
        elif len(rod_cislo) == 10:
            if int(rod_cislo[0:2]) >= 26:
                return False
            elif rod_cislo[2:4] >= "13" or rod_cislo[2:4] == "00" or rod_cislo[4:6] >= "32" or rod_cislo[4:6] == "00":
                return False
            elif str(int(rod_cislo)/11)[-1] != "0":
                return False
        return True