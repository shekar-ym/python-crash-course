from pathlib import Path
import json

path = Path('fav_num2.json')

if path.exists():
    contents = path.read_text()
    fav_num2 = json.loads(contents)
    print(f"Your fav number is {fav_num2}")
else:
    fav_num2 = input("Enter your favourite number: ")
    contents = json.dumps(fav_num2)
    path.write_text(contents)

