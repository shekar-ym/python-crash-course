
from user import User

class Admin(User):
    """This class inherits User class with its own set of attributes and methods"""
    def __init__(self, first_name, last_name, age, city, country):
        super().__init__(first_name, last_name, age, city, country)
        self.privileges = Privileges()

class Privileges:
    """Separate class to store privileges of a user and display the details"""
    def __init__(self,privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin user has following privileges")
        for privilege in self.privileges:
            print(f"- {privilege}")