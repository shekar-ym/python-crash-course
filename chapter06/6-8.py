pluto = {
    'type': 'dog',
    'owner': 'madhan'
}

gunda = {
    'type': 'dog',
    'owner': 'arvind'
}

missy = {
    'type': 'cat',
    'owner': 'sheldon'
}

cinnamon = {
    'type': 'dog',
    'owner': 'rajesh'
}

pets = [gunda, pluto, missy, cinnamon]

for pet in pets:
    for key, value in pet.items():
        pet_type = pet['type']
        pet_owner= pet['owner']
    print(f"{pet_owner} has a {pet_type}")