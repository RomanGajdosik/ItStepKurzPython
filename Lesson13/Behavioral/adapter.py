class LegacyClass:
    def legacy_method(self):
        print("Legacy method called")

# Cieľové rozhranie
class Target:
    def new_method(self):
        pass

# Trieda Adaptéra
class Adapter(Target):
    def __init__(self):
        self.legacy_object = LegacyClass()

    def new_method(self):
        self.legacy_object.legacy_method()

# Použitie adaptéra
adapter = Adapter()
adapter.new_method()

