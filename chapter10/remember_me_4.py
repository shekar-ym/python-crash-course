from pathlib import Path
import json

def get_stored_username(path):
    """Get stored user name if available"""
    if path.exists():
        contents=path.read_text()
        user_name=json.loads(contents)
        return user_name
    else:
        return None

def greet_user():
    """Greet user by their name"""
    path = Path('username4.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input("Enter your user name: ")
        contents= json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you are back, {username}")

greet_user()
