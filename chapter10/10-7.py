print("Enter two numbers")
print("Enter 'q' to quit")

while(True):
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        sum_number =int(first_number) + int(second_number)
    except ValueError:
        print("You entered string. Please enter a number")
    else:
        print(sum_number)