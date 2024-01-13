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
        self.number_served = 5000
    
    def open_restaurant(self):
        """Method to print a message that restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open !!")

fav_restaurant = Restaurant('mtr','South Indian')
fav_restaurant.describe_restaurant()

fav_restaurant.number_served = 4500
fav_restaurant.describe_restaurant()

fav_restaurant.set_number_served(5000)
fav_restaurant.describe_restaurant()



