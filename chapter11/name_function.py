def get_formatted_name(first,last, middle=''):
    """Function to return a formatted name based on first and last names"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()