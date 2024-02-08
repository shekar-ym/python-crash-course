from pathlib import Path
import json

# user_name = input("Enter your user name: ")
# age = input("Enter your age: ")
# location = input("Enter your city: ")

# user_info = {'user_name' : user_name,
#              'age': age,
#              'location': location
#              }

path = Path('user_info.json')
# contents = json.dumps(user_info)
# path.write_text(contents)

contents = path.read_text()
user_info = json.loads(contents)
print("Welcome back.")
print(f"Your user name is {user_info['user_name']}.")
print(f"Your age is {user_info['age']} years.")
print(f"Your location is {user_info['location']}.")