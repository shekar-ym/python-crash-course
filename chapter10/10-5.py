from pathlib import Path

name = ''
guest_list = ''
while(True):
    name = input("Enter the name of the guest: ")
    if name == 'quit':
        break
    guest_list += name + "\n"

path = Path('guest_list.txt')
path.write_text(guest_list)