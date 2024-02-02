print("Enter two numbers")

first_number = input("First number: ")
second_number = input("Second number: ")
try:
    sum_number =int(first_number) + int(second_number)
except ValueError:
    print("You entered string. Please enter a number")
else:
    print(sum_number)