print("Welcome to the Roller Coaster ride")
height = int(input("What is your height?:"))
bill = 0

if height >= 120 :
    print("You can ride the Roller Coaster")
    age = int(input("What is your age ? "))
    if age <=5 :
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18 :
        bill = 7
        print("Tickets for teens cost $7.")
    elif age >= 45 and age <=55 :
        bill = 0
        print("Go on and have a free ride. Try to enjoy your life.")
    else :
        bill = 12
        print("Adult tickets are $12.")


    photo = input("Do you want to take photo ? (type y for yes & n for no)")
    if photo == "y" :
        bill += 3

    print(f"Your total bll = ${bill}")

else :
    print("To ride the roller coaster you have to grow taller")