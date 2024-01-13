class Car:
    """Class to describe a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        "Method to generate a descriptive name of the car"
        descriptive_name = f"{self.make.title()} {self.model.title()} {self.year}"
        print(descriptive_name)

my_new_car = Car('Tesla', 'Model 3', 2021)
my_new_car.describe_car()