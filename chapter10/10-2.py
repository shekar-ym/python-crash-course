from pathlib import Path

path = Path('/workspaces/python-crash-course/chapter10/learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()

about_python = ''

for line in lines:
    line = line.replace('Python','C')
    about_python += line

print(about_python)
