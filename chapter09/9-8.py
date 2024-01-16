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

class Admin(User):
    """This class inherits User class with its own set of attributes and methods"""
    def __init__(self, first_name, last_name, age, city, country):
        super().__init__(first_name, last_name, age, city, country)
        self.privileges = Privileges()

class Privileges:
    """Separate class to store privileges of a user and display the details"""
    def __init__(self,privileges):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin user has following privileges")
        for privilege in self.privileges:
            print(f"- {privilege}")

chandra_user = Admin('chandrashekar', 'y m', 40, 'sydney', 'australia')
chandra_user.describe_user()