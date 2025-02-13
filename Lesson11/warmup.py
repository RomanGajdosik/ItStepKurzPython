# 1 cm = 0.0328084 feet

class Konvertuj:

    @staticmethod
    def cm_na_feet(vstup):
        premennaf = 0.0328084
        return '{0:.7f}'.format(vstup * premennaf )

    @staticmethod
    def feet_na_cm(vstup):
        premennacm = 30.48
        return '{0:.7f}'.format(vstup / premennacm)

print(Konvertuj.cm_na_feet(20))
print(Konvertuj.feet_na_cm(10))