def describe_pets(pet_name,pet_type='dog'):
    """Default values"""
    print(f"I have a {pet_type}")
    print(f"And it's name is {pet_name.title()}")

describe_pets('cinnamon')

describe_pets(pet_name = 'gunda',pet_type = 'cat')
describe_pets('pluto','dog')