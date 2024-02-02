from pathlib import Path

def print_animal(path):
    """Function to print the contents of a animal text file"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f"File {path} not found")
        pass
    else:
        lines = contents.splitlines()
        print(f"Names of animals in file {path} are:")
        for line in lines:
            print(line)

file_names = ['chapter10/cats.txt', 'chapter10/dogs.txt']
for file_name in file_names:
    path = Path(file_name)
    print_animal(path)
