buffet = ('biryani', 'Sambar','rice', 'jamoon', 'pappad')

print('\nItems offered in the buffet are:\n')
for item in buffet:
    print(item.title())

# buffet[1] = 'rasam'

buffet = ('biryani', 'Sambar','rasam', 'rasmalai', 'pappad')

print('\nUpdated tems offered in the buffet are:\n')
for item in buffet:
    print(item.title())