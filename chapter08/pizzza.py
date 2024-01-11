def make_pizzza(size, *toppings):
    """Function to accept toppings and print all  toppings being added to pizza"""
    print(f"Making a {size} size pizza with the following toppings")
    for topping in toppings:
        print(f"Adding {topping} to the pizza")