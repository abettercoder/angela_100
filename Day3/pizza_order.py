print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want?")
add_pepperoni = input("Would you like pepperoni? (y/n)")
extra_cheese = input("Would you like extra cheese? (y/n)")

price = 0
if size == "small":
    price = 15
    if add_pepperoni == "y":
        price += 2
    if extra_cheese == "y":
        price += 1
elif size == "medium":
    price = 20
    if add_pepperoni == "y":
        price += 3
    if extra_cheese == "y":
        price += 1
elif size == "large":
    price = 25
    if add_pepperoni == "y":
        price += 3
    if extra_cheese == "y":
        price += 1
else:
    print("Sorry, we don't have that size.")

print("Your total bill is $" + str(price) + ".")