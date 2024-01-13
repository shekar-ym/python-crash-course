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

my_used_car = Car('Tesla', 'model y', 2023)
my_used_car.describe_car()


my_used_car.update_odometer(34000)
my_used_car.read_odemeter()

my_used_car.incremment_odometer(400)
my_used_car.read_odemeter()