fav_lang = {
    'chandra': 'python',
    'varun': 'sql',
    'madhan': 'python',
    'arvind': 'c++'
}

for name,language in fav_lang.items():
    print(f"{name.title()}'s fav language is {language.title()}")

print("\n")

for name in fav_lang.keys():
    print(name.title())

print("\n")

for language in fav_lang.values():
    print(language.title())

print("\n")

for language in sorted(fav_lang.values()):
    print(language.title())

print("\n")

for language in set(fav_lang.values()):
    print(language.title())