usernames = ['admin','shekar.ym','balu2gani','shekar026','harold.finch1702']

if usernames == []:
    print("We need to find some users!")

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f"Hello {username}, thank you for logging in again.")