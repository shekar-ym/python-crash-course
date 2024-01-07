responses = {}
polling_active = True

while polling_active:
    name = input('What is your name? : ')
    # age = int(input('What is your age'))
    hobby = input('What is your hobby? : ')

    responses[name] = hobby

    repeat = input('Would you like another person to respond to poll? ')
    if repeat == 'No':
        polling_active = False

print(responses)

for key,value in responses.items():
    print(f"{key.title()}'s hobby is {value}")