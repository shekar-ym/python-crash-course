def make_pizza(size, *toppings):
    """Function to accept toppings and print all  toppings being added to pizza"""
    print(f"Making a {size} size pizza with the following toppings")
    for topping in toppings:
        print(f"Adding {topping} to the pizza")

make_pizza('small','olives')
make_pizza('large','pineapple', 'mushrooms', 'jalepenos', 'panner')