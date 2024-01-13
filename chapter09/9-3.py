class User:
    """Class to model a user profile"""

    def __init__(self,first_name,last_name,age,city,country):
        """Method initiating a user profile """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country

    def describe_user(self):
        "Method to describe a user by printing user details"
        print(f"User's full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"User is {self.age} yeard old.")
        print(f"User is from {self.city.title()} which is in {self.country.title()}.")

    def greet_user(self):
        """Method to greet the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}. Good morning.")



arvind_user = User('arvind', 'm', 40, 'bengaluru','india')
madhan_user = User('madhan', 't',41, 'chicago','usa')
varun_user = User('varun', 'v', 39,'california','usa')

arvind_user.describe_user()
arvind_user.greet_user()

madhan_user.describe_user()
madhan_user.greet_user()

varun_user.describe_user()
varun_user.greet_user()