print("Welcome to the Tip Calculator")
bill_amount = float(input("What was the total bill?\n"))
tip_percent = float(input("How much tip would you like to give ? 10 , 12 or 15 ?\n"))
number_of_people = int(input("How many people to split the bill ?\n"))
total_pay_amount = bill_amount + (( bill_amount * tip_percent ) / 100)
each_person_pay = round(total_pay_amount / number_of_people , 2)

print(f"Each person should pay : {each_person_pay}")