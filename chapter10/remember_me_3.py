from pathlib import Path
import json

def greet_user():
    """Greet user by name"""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}")
    else:
        username = input("Enter your username: ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you are back, {username}")


greet_user()