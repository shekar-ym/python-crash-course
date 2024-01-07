def describe_pets(pet_type,pet_name):
    """Positional Arguments"""
    print(f"I have a {pet_type}")
    print(f"And it's name is {pet_name.title()}")

describe_pets('dog', 'pluto')
describe_pets('cat','missy')