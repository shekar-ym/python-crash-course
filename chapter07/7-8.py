sandwich_orders = ['paneer sandwich', 'pastrami','vegetable sandwich', 'egg sandwich','pastrami', 'chicken sandwich', 'pastrami']

finished_sandwiches = []

print("We have run out of pastrami sandwiches\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    preparing_now = sandwich_orders.pop()
    print(f"Preparing your {preparing_now} now")

    finished_sandwiches.append(preparing_now)


for sandwich in finished_sandwiches:
    print(f"\nYour order of {sandwich} is now ready !!")