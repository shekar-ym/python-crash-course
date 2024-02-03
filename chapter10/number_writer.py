from pathlib import Path
import json

numbers = [1,2,45,64,54,32,63,163,3,35]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)