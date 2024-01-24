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

    def read_odemeter(self):
        """Method to read odemter readimg"""
        print(f"The car's current odometer reading is {self.odometer_reading}")

my_new_car = Car('tesla','model 3','2021')
my_new_car.describe_car()
my_new_car.read_odemeter()

my_new_car.odometer_reading = 37000
my_new_car.describe_car()
my_new_car.read_odemeter()