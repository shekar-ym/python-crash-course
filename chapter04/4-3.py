for value in range(1,21):
    print(value)

one_million = []
for value in range(1,1000001):
    one_million.append(value)

print(one_million)

print(min(one_million))
print(max(one_million))
print(sum(one_million))

odd_numbers=[]
for value in range(1,20,2):
    print(value)
    odd_numbers.append(value)
print(odd_numbers)

multiple3=[]
for value in range (3,30,3):
    print(value)
    multiple3.append(value)
print(multiple3)

cubes = []
for value in range(1,11):
    print(value ** 3)
    cubes.append(value ** 3)
print(cubes)

cubes2 = [value ** 3 for value in range(1,11)]
print(f"cubes2:\n {cubes2}")