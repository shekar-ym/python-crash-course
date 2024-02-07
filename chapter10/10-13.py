from pathlib import Path
import json

user_name = input("Enter your user name: ")
age = input("Enter your age: ")
location = input("Enter your city: ")

user_info = {'user_name' : user_name,
             'age': age,
             'location': location
             }

print(user_info)