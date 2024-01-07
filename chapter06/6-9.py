favorite_places = {
    'arvind': ['malaysia','bengaluru','mysore'],
    'varun':['california','bengaluru'],
    'madhan': ['chennai','london','chicago'],
}

for name,places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
