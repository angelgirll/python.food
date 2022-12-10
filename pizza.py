small = 15
medium = 20
large = 25
order = 0
pizza_ordered = input("How much is pizza?(1 : small = 15 , 2 : medium = 20, 3 : large = 25) => ")
print(pizza_ordered)
if pizza_ordered == "3":
    order = + large
    print("Recharge your large!", order)
elif pizza_ordered == "2":
    order = + medium
    print("Recharge your medium!", order)
else:
    order = +  small
    print("Recharge your small", order)
peproni = input("aya peproni mikhi ? y or n")
if peproni == 'y':
    if pizza_ordered == '2':
        order += 3
        print(order)
    elif pizza_ordered == '3':
        order += 3
        print(order)
    else:
        pizza_ordered += 2
        print(order)
panire = input("aya panire mikhie ? y or n")
if panire == 'y':
    order += 1
    print('price', order)
else:
    print(order)
