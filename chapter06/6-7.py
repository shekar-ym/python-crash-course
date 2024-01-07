chandra = {
    'first_name': 'Chandrashekar', 
    'last_name': 'Yelahanka Munikrishna',
    'age': 40,
    'city':'Bangalore'
}

sri = {
    'first_name': 'Srilekha', 
    'last_name': 'Mekala',
    'age': 34,
    'city':'Bangalore'
}

bhumi = {
    'first_name': 'Bhumi', 
    'last_name': 'Chandrashekar',
    'age': 6,
    'city':'Grand Rapids'
}

my_family = [chandra, sri, bhumi]

for member in my_family:
    for key,value in member.items():
        full_name = f"{member['first_name']} {member['last_name']}"
        age = f"{member['age']}"
        city = f"{member['city']}"
    print(f"{full_name}")
    print(f"{age}")
    print(f"{city}\n")


