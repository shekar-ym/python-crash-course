from pathlib import Path

path = Path('/workspaces/python-crash-course/chapter10/learning_python.txt')

contents = path.read_text()

# print(contents)

lines = contents.splitlines()
whole_string = ''

for line in lines:
    whole_string += line.strip()

print(whole_string)


