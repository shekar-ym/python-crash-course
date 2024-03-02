class Employee:
    """Class to define and manage employee details."""

    def __init__(self,first_name, last_name, annual_salary):
        """Store Employee details"""
        self.firt_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount):
        if raise_amount:
            new_annual_salary = self.annual_salary + raise_amount
        else:
            new_annual_salary = self.annual_salary + 5000
        return new_annual_salary
