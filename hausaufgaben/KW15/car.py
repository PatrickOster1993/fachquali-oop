class Car:
    def __init__(self):
        self.brakes = "DiscBrakes"
        self.gas_pedal = True
        self.engine = "FuelInjected"
        self.transmission = "FiveSpeed"

    def steer(self):
        print("Car is steering")

    def change_gears(self):
        print("Car changes gears")

    def apply_brake(self):
        print("Brakes applied")

    def adjust_brake(self):
        print("Brakes adjusted")

    def change_oil(self):
        print("Oil changed")


class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        self.car.steer()
        self.car.change_gears()
        self.car.apply_brake()


class Mechanic:
    def __init__(self, car):
        self.car = car

    def maintain(self):
        self.car.adjust_brake()
        self.car.change_oil()
