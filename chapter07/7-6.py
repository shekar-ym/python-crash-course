prompt = input("Enter your age: ")


while prompt != 'quit':
    if prompt == 'quit':
        break
    age = int(prompt)
    if age >= 3 and age<=12:
        print("You ticket cost is $10")
        break
    elif age > 12:
        print("Your ticket cost is $15")
        break