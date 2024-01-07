dream_vacations = {}
polling_active = True

while polling_active:
    name = input('What is your name? : ')
    response = input('If you could visit one place in the world,' 
    'where would you go?: ')

    dream_vacations[name] = response

    repeat = input("Would you like other person to take this poll? Yes / No: ")
    if repeat == 'No':
        break


for key,value in dream_vacations.items():
    print(f"\n{key.title()}'s dream vacation is {value}. ")