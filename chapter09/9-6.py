class Restaurant:
    """Class defining a resturant and availbale cuisines"""
    def __init__(self,restaurant_name, cuisine_type):
        """Initiating restuarant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Method to print the resturant details"""
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"Speciality cuisine here is {self.cuisine_type}.")
        print(f"Number of people served: {self.number_served}.")

    def set_number_served(self,number_served):
        """Method to update the number of people served"""
        self.number_served = number_served
    
    def open_restaurant(self):
        """Method to print a message that restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open !!")

class IceCreamStand(Restaurant):
    """This class inherits from Restuarant class and will have its own attributes and methods"""
    def __init__(self,restaurant_name,cuisine_type):
        """Initializing the IceCreamStand class with its own attributes and methods"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Mango', 'Pistacio']

    def display_flavors(self):
        """Method to print flavors of available ice cream"""
        print(f"Following flavors of ice cream are available")
        for flavor in self.flavors:
            print(f"- {flavor}")


new_icecream_stand = IceCreamStand('mtr','South Indian')
new_icecream_stand.set_number_served(500)
new_icecream_stand.describe_restaurant()
new_icecream_stand.display_flavors()