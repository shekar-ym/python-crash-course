cities = {
    'bengaluru':{
        'country': 'India',
        'population': '10 million',
        'fact': 'Silicon valley of India',
    },
    'sydney':{
        'country': 'Australia',
        'population': '25 million',
        'fact': 'largest city in Australia',
    },
    'helsinki':{
        'country': 'Finland',
        'population': '5 million',
        'fact': 'capital city of Finland',
    },
}

for city,city_info in cities.items():
    
    country=f"{city_info['country']}"
    population=f"{city_info['population']}"
    fact=f"{city_info['fact']}"

    print(f"{city.title()} is a city in {country}, has a population"
    f" of {population} and is {fact}")