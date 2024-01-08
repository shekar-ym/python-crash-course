def formatted_name(first_name,last_name):
    """function to construct a formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Enter q at any time to quit. Press enter now")
    
    
    first_name = input("Enter your First Name: ")
    if first_name == 'q':
        break
    last_name = input("Enter your Last Name: ")
    if last_name == 'q':
        break

    scientist_name = formatted_name(first_name, last_name)
    print(f"Good morning, {scientist_name}")





