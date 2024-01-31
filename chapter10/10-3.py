from pathlib import Path
path = Path('/workspaces/python-crash-course/chapter10/learning_python.txt')
contents = path.read_text()

read_text = ''

for line in contents.splitlines():
    read_text += line.strip()

print(read_text)
    