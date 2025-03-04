class Singleton:
    # Premenná triedy, zdieľaná medzi všetkými objektmi tejto triedy
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Táto trieda je Singleton a už bola inštancovaná!")
        else:
            self.meno = "Patrik"
            Singleton._instance = self

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

# Testovanie Singletonu
s1 = Singleton.getInstance()
print(s1.meno)

s2 = Singleton.getInstance()
s1.meno = "Milan"
print(s2.meno)