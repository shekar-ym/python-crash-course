from random import choice

inputs = (1,2,3,4,5,6,7,8,9,0,'I', 'A','U','F')

print("Any ticket matching these 4 numbers or letters wins a prize.")
i=1
while(i<=4):
    print(f"Nuimber {i} matching number/letter is {choice(inputs)} ")
    i+=1



