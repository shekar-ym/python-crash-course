class Restaurant:
    """Class defining a resturant and availbale cuisines"""
    def __init__(self,restaurant_name, cuisine_type):
        """Initiating restuarant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Method to print the resturant details"""
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"Speciality cuisine here is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Method to print a message that restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open !!")

fav_restaurant = Restaurant('mtr','South Indian')
print(f"Restaurant name is {fav_restaurant.restaurant_name.title()}")
print(f"This restaurant's speciality cuisine is {fav_restaurant.cuisine_type}")

fav_restaurant.describe_restaurant()
fav_restaurant.open_restaurant()
