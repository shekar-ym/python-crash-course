prompt = input("Enter your age: ")
age = int(prompt)

while True:
    if age >= 3 and age<=12:
        print("You ticket cost is $10")
        break
    elif age > 12:
        print("Your ticket cost is $15")
        break
    else: 
        continue