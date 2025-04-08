class Driver:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def steering(self, car):
        print("Driver is using the steering wheel.")
        car.steer()

    def up_shift(self, car):
        print("Driver is shifting up.")
        car.change_gears()

    def slow_down(self, car):
        print("The Driver slows down the car.")
        car.apply_brake()

    


class Mechanic:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def inspect_brake(self, car):
        print("The mechanic has inspected the brakes.")
        car.adjust_brake()

    def change_fluids(self, car):
        print("The mechanic has inspected the fluids.")
        car.change_oil()



class Car:

    def __init__(self):
        self.brakes = "DiscBrakes"
        self.gas_pedal = 0
        self.engine = "FuelInjected"
        self.transmission = "FiveSpeed"

    def steer(self):
        print("The car is turning.")

    def change_gears(self):
        print("The gear has changed.")

    def apply_brake(self):
        print("The brake is being applied.")

    def adjust_brake(self):
        print("The brake has been adjusted.")

    def change_oil(self):
        print("The oil has been changed.")


    def __str__(self):
        pass




car1 = Car()

driver1 = Driver()

mechanic1 = Mechanic()

driver1.slow_down(car1)

mechanic1.change_fluids(car1)