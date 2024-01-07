to_see = ['london', 'kenya', 'brazil', 'tokyo', 'dubai']
print(f"List in original order: \n{to_see}")

print(f"Ordered list: \n{sorted(to_see)}")

print(f"List in original order: \n{to_see}")

print(f"Reverse Ordered list: \n{sorted(to_see, reverse=True)}")

print(f"List in original order: \n{to_see}")

to_see.reverse()
print(f"Reversed list:\n{to_see}")

to_see.reverse()
print(f"Original order list:\n{to_see}")

to_see.sort()
print(f"Permanently sorted list:\n{to_see}")

to_see.sort(reverse=True)
print(f"Permanently reversed alphabetically sorted list:\n{to_see}")


print(f"I am going to have dinner at {len(to_see)} places")