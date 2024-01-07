invited = ['PRK', 'SPB', 'SSRS']
print(f"Please come to the dinner sir, {invited[0]}")
print(f"Please come to the dinner god, {invited[1]}")
print(f"Please come to the dinner guru. {invited[2]}")

print(f"{invited[0]} cannot be make it to dinner")

del(invited[0])

print(f"Please come to the dinner sir, {invited[0]}")
print(f"Please come to the dinner god, {invited[1]}")

print("A new bigger table is available for us")

invited.insert(0, 'MS Narayana')
invited.insert(2, 'Dharmavarapu')
invited.append('Veturi')

print(f"Please come to the dinner sir, {invited[0]}")
print(f"Please come to the dinner god, {invited[1]}")
print(f"Please come to the dinner guru. {invited[2]}")
print(f"Please come to the dinner sir, {invited[3]}")
print(f"Please come to the dinner god, {invited[4]}")

print("Apologies !!, i can invite only 2 people for dinner")

print(f"Current list {invited}")


popped_invitee = invited.pop()
print(f"Sorry sir {popped_invitee}. I cannot invite you for dinner")
popped_invitee = invited.pop()
print(f"Sorry sir {popped_invitee}. I cannot invite you for dinner")
popped_invitee = invited.pop()
print(f"Sorry sir {popped_invitee}. I cannot invite you for dinner")

print(f"Current list {invited}")

print(f"Sir, please dont forget the invitation for dinner {invited[0]}")
print(f"Sir, please dont forget the invitation for dinner {invited[1]}")

del invited[0]
del invited[0]

print(invited)
