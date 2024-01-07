pizzas = ['Mac n Cheese', 'Chicken Supreme', 'Paneer Sensation', 
'Veggie sensation', 'BBQ chicken', 'Vegan Pizza', 'Garlic Prawn']

print(f"The first three items in the list are:\n{pizzas[:3]}")
print(f"Three items from the middle of the list are:\n{pizzas[3:6]}")
print(f"The last three items in the list are:\n{pizzas[-3:]}")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('Maccaroni')
friend_pizzas.append('Spicy Paneer')

print(pizzas)
print(friend_pizzas)

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


print("\nUsing for loop. My favorite foods are:")
for food in my_foods:
    print(food)

print("\nUsing for loop. My friend's favorite foods are:")
for food in friend_foods:
    print(food)
