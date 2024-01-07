rivers = {
    'india': 'Ganga',
    'egypt': 'nile',
    'australia': 'murray',
}

for key,value in rivers.items():
    print(f"The {value.title()} runs through {key.title()}")

print("\n")

for key in rivers.keys():
    print(key.title())

print("\n")

for value in rivers.values():
    print(value.title())

