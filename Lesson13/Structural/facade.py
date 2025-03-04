class Osvetlenie:
    def zapni(self):
        print("Osvetlenie zapnute")

    def vypni(self):
        print("Osvetlenie vypnute")

class Klimatizacia:
    def zapni(self):
        print("Klimatizacia zapnuta")

    def vypni(self):
        print("Klimatizacia vypnuta")

class AudioSystem:
    def zapni(self):
        print("Audio system zapnuty")

    def vypni(self):
        print("Audio system vypnuty")

class DomacaAutomatizaciaFacade:
    def __init__(self):
        self.osvetlenie = Osvetlenie()
        self.klimatizacia = Klimatizacia()
        self.audio_system = AudioSystem()

    def vecernyRezim(self):
        self.osvetlenie.zapni()
        self.klimatizacia.vypni()
        self.audio_system.zapni()

    def odchodZDomu(self):
        self.osvetlenie.vypni()
        self.klimatizacia.vypni()
        self.audio_system.vypni()

dom_automatizacia = DomacaAutomatizaciaFacade()
dom_automatizacia.vecernyRezim()
dom_automatizacia.odchodZDomu()




