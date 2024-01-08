def build_person_dictionary(first_name, last_name, age=None):
    person_dictionary = {
        'first_name': first_name.title(),
        'last_name': last_name.title(),
    }
    if age:
        person_dictionary [age] = age
    return person_dictionary

scientist = build_person_dictionary('Albert', 'Einstein', '100')
print(scientist)

musician = build_person_dictionary('jimi', 'hendrix')
print(musician)