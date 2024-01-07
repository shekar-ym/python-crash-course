prompt = "Enter a topping you want on your pizza: "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")