from pathlib import Path
import json

path = Path('fav_num.json')

fav_number = input("Enter your favorite number: ")
contents = json.dumps(fav_number)
path.write_text(contents)