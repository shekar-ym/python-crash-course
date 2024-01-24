class Car:
    """Class to describe a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def describe_car(self):
        "Method to generate a descriptive name of the car"
        descriptive_name = f"{self.make.title()} {self.model.title()} {self.year}"
        print(descriptive_name)

    def update_odometer(self,mileage):
        """Method to update the odometer_reading and reject any update to odemter reading
        less than current reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer reading to a lower value")

    def incremment_odometer(self,miles):
        """Method to increment odometer reading by miles """
        self.odometer_reading += miles

    def read_odemeter(self):
        """Method to read and print odemeter reading """
        print(f"The car's current odometer reading is {self.odometer_reading}")


class Battery():
    """Class to model Battery with its own set of attributes and methods"""
    def __init__(self,battery_size = 40):
        """Initiazlizing the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self,battery_size):
        """Method to describe battery attributes"""
        print(f"This car comes with {battery_size}-kWh battery")

    def get_range(self,battery_size):
        """Determine range, the car provides based on battery size and print the same"""
        if battery_size == 40:
            range = 150
        elif battery_size == 65:
            range = 250
        print(f"With {battery_size}-kWh battery, this car provides a range of {range} miles")

class ElectricCar(Car):
    """Class to define an Electric car, by inheriting from Car class"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_byd = ElectricCar('byd','dolphin',2023)
my_byd.describe_car()
my_byd.battery.describe_battery(40)
my_byd.battery.get_range(40)