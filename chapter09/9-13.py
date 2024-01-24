from random import randint

class Die:
    """a sample class to define a die and its attributes"""
    def __init__(self,sides):
        self.sides = sides
    
    def roll_die(self):
        print(f"Result of rolling the die : {randint(1,self.sides)}")


six_sided_die = Die(6)
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()


ten_sided_die = Die(10)
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()


twenty_sides_die = Die(20)
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()
twenty_sides_die.roll_die()