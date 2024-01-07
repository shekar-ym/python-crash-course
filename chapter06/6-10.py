fav_numbers = {
    'chandra': [17,2,1983],
    'varun': [22,3,1984],
    'madhan': [31,1,1983],
    'arvind': [13,1,1983],
}

for name,numbers in fav_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")