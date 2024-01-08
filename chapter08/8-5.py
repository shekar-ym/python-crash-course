def describe_city(name,country='Australia'):
    print(f"{name.title()} is in {country.title()}")

describe_city('sydney')
describe_city('melbourne')
describe_city('auckland', 'newzealand')     