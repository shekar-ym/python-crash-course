def build_profile(first_name, last_name, **user_info):
    """Buiild the user profile dictionary using the first name, 
    last name and other user info"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('Chandra', 'Y M', location = 'Sydney', study = 'Coding')
print(user_profile)