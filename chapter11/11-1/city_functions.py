def get_city_details(city_name, country_name, population = ''):
    """Function to return city details in the format City, Country, such as 'Santiago, Chile'"""

    if population:
        city_details = f"{city_name}, {country_name} - population {population}"
    else:
        city_details = f"{city_name}, {country_name}"
    return city_details.title()