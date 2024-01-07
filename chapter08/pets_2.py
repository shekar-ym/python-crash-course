def describe_pets(pet_type,pet_name):
    """Keyword Arguments"""
    print(f"I have a {pet_type}")
    print(f"And it's name is {pet_name.title()}")

describe_pets(pet_type = 'dog', pet_name = 'pluto')

describe_pets(pet_name = 'missy', pet_type='cat')