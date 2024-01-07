number = input("Enter a number ")
number_int = int(number)

if number_int % 10 == 0:
    print(f"{number_int} is a multiple of 10")
else:
    print(f"{number_int} is a NOT multiple of 10")