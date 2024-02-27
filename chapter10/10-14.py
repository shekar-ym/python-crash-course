from pathlib import Path
import json

def get_stored_username(path):
    """Get stored user name if available"""
    if path.exists():
        contents = path.read_text()
        user_name = json.loads(contents)
        return user_name
    else:
        return None

def get_new_username(path):
    "Prompt for a new user name"
    user_name = input("What is your user name? ")
    contents = json.dumps(user_name)
    path.write_text(contents)
    return user_name

def greet_user():
    """Greet user by name"""
    path = Path('username5.json')
    user_name = get_stored_username(path)
    print(user_name)
    user_respone = input("Is this your user name, Yes or No? ")
    if user_respone == "Yes":
        print(f"Welcome back, {user_name}")
    else:
        user_name = get_new_username(path)
        print(f"We will remember you when you are back, {user_name}")

greet_user()

