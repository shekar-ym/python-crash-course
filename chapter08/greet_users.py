def greet_users(names):
    """Function to greet a list of users"""
    for name in names:
        print(f"Hello, {name.title()}")

users = ['bhumi', 'ira', 'anhad']
greet_users(users)