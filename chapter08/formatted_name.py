def formatted_name(first_name,last_name):
    """function to construct a formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

scientist_name = formatted_name('Albert', 'Einstein')
print(scientist_name)



def formatted_name_v2(first_name,last_name,middle_name =''):
    if middle_name:
        full_name_v2 = f"{first_name} {middle_name} {last_name}"
        return full_name_v2.title()
    else:
        full_name_v2 = f"{first_name} {last_name}"
        return full_name_v2.title()

scientist_name_v2 = formatted_name_v2('Albert', 'Einstein')
print(scientist_name_v2)

scientist_name_v2 = formatted_name_v2('john', 'hooker', 'lee')
print(scientist_name_v2)
