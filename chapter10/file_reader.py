from pathlib import Path

# path = Path('pi_digits.txt')

# path = Path('/workspaces/python-crash-course/chapter10/pi_digits.txt')
# contents = path.read_text()
# # print(contents)


# lines = contents.splitlines()
# pi_string = ''
# # for line in lines:
# #     print(line)

# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

path = Path('/workspaces/python-crash-course/chapter10/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}.....")
print(len(pi_string))


