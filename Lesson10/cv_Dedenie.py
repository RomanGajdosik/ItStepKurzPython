class Vehicle:
    def __init__(self,vehicleId,vehicleName,vehicleType):
        self.vehicleId = vehicleId
        self.vehicleName = vehicleName
        self.vehicleType = vehicleType
    def showName(self):
        print(f'Nazov vozidla : {self.vehicleName}')

class Car(Vehicle):
    def __init__(self,vehicleId,vehicleName,vehicleType,carModel):
        super().__init__ (vehicleId,vehicleName,vehicleType)
        self.carModel = carModel
    def showName(self):
        print(f'Nazov vozidla v objekte Car {self.vehicleName}')
class Bus(Vehicle):
    def __init__(self,vehicleId,vehicleName,vehicleType,busModel):
        super().__init__(vehicleId,vehicleName,vehicleType)
        self.busModel = busModel

mhd =Bus(1,'Linka cislo 1','bus','karosa')
osobne_Auto = Car(2,'Auto 1','osobne','scala')

osobne_Auto.showName()
mhd.showName()
