class User:
    """Class to model a user profile"""

    def __init__(self,first_name,last_name,age,city,country):
        """Method initiating a user profile """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        "Method to describe a user by printing user details"
        print(f"User's full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"User is {self.age} yeard old.")
        print(f"User is from {self.city.title()} which is in {self.country.title()}.")
        print(f"Number of login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        """Method to increment login attempt count"""
        self.login_attempts += 1

    def reset_login_count(self):
        """Method to reset login attempt count"""
        self.login_attempts = 0 

    def greet_user(self):
        """Method to greet the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}. Good morning.")

