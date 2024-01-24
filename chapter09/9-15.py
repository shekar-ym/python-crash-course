from random import choice

my_ticket =(5,3,'F',5)
inputs = (1,2,3,4,5,6,7,8,9,0,'I', 'A','U','F')

trial_count = 0

won_ticket = []
while(my_ticket != won_ticket):
    i=1
    won_ticket = []
    while(i<=4):
        won_ticket.append(choice(inputs))
        i+=1
    trial_count+=1
    print(won_ticket)
    print(f"trial count: {trial_count}")

print(f"Loop had to run {trial_count} times for you to win a lottery")