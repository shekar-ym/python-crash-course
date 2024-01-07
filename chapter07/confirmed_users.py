uncofirmed_users = ['chandra','sri','bhumi','meera']
confirmed_users = []

while uncofirmed_users:
    current_user = uncofirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")

    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(f"\n{confirmed_user.title()} is now verified")