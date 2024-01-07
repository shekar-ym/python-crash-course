# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

lang = ['kannada', 'telugu', 'english', 'hindi', 'tamil']

lang.append('marathi')

print(lang)

lang.insert(2, 'odiya')

print(lang)

del lang[2]
print(lang)

lang.pop()
print(lang)

popped_language = lang.pop()
print(lang)
print(popped_language)

print(f"the last language i learnt was {popped_language}")

first_language = lang.pop(0)
print(lang)
print(f"the first languge i learnt was {first_language}")

lang.remove('hindi')
print(lang)

lang.append('bengali')
lang.append('urdhu')
lang.append('finnish')

print(lang)
lang.sort()

print(f"sorted lang list\n{lang}")

lang.append('swedish')
print(lang)

print(f"temp sorted lang list\n{sorted(lang)}")
print(f"list without temp sorting\n{lang}")


print(lang)
lang.reverse()
print(lang)

print(f"length of list = {len(lang)}")