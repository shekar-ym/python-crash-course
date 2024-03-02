from city_functions import get_city_details

def test_city_country():
    """Does this test return city details in format 'Santiago, Chile'"""
    city_details_test = get_city_details('santiago','chile')
    assert city_details_test == 'Santiago, Chile'


def test_city_country_population():
    """Does this test return city detauls in format 'Santiago, Chile - population 5000000"""
    city_pop_details_test=get_city_details('santiago','chile',5000000)
    assert city_pop_details_test == 'Santiago, Chile - Population 5000000'