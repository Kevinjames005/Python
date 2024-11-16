print("Welcome to the Python Pizza Deliveries !!")
size = input("What size of pizza do you want ! Do you want small , medium or large ")
pepperoni = input("Do you want pepperoni , (yes or no)")
extra_cheese = input("Do you want extra cheese , (yes or no)")
bill = 0

if size == "small" :
    bill = 15
    if pepperoni == "yes" :
        bill += 2
    if extra_cheese == "yes" :
        bill += 1
elif size == "medium" :
    bill = 20
    if pepperoni == "yes" :
        bill += 3
    if extra_cheese == "yes" :
        bill += 1
elif size == "large" :
    bill = 25
    if pepperoni == "yes" :
        bill += 3
    if extra_cheese == "yes" :
        bill += 1
else :
    print("There is no such choice")

print(f"The total bill for your order is $ {bill}")



