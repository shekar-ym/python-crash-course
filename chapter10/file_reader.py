from pathlib import Path

# path = Path('pi_digits.txt')

path = Path('/workspaces/python-crash-course/chapter10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)


# print(contents)