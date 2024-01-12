class Dog:
    """A simple class to modela Dog"""
    def __init__(self,name,age):
        """Initalize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command""" 
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Simulate rolling over in responsea to a command"""
        print(f"{self.name.title()} rolled over")     

madhan_dog = Dog('pluto', 6)
print(f"Madhan's dog name is {madhan_dog.name.title()}.")
print(f"{madhan_dog.name.title()}'s age is {madhan_dog.age} years") 

madhan_dog.sit()
madhan_dog.roll_over()


arvind_dog = Dog('gunda',8)
arvind_dog.sit()
arvind_dog.roll_over()

print(arvind_dog)