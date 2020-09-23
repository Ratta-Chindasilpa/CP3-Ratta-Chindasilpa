class Vehicle:
    lecenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle): #ใส่classที่จะสืบทอด #เป็น class ลูก
    def sayHello(self):
        print("Hello World!")

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass
    '''lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")'''

class EstateCar(Vehicle):
    pass
    '''lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")'''

pickUp1 = Pickup()
pickUp1.turnOnAirConditioner()

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = EstateCar()
estatecar1.turnOnAirConditioner()

