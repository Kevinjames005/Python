import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
letter_number = int(input("How many letters would you like in the password.\n"))
symbol_number = int(input("How many symbols do you want in the password.\n"))
number_number = int(input("How many numbers do you want in the password.\n"))
password = ''
choice = input("What type of password do you want, Easy or Hard\n").lower()
for i in range(1, letter_number + 1):
    password = password + random.choice(letters)
for j in range(1, symbol_number + 1):
    password = password + random.choice(symbols)
for k in range(1, number_number + 1):
    password = password + random.choice(numbers)

if choice == "easy" :
#Easy
    print(f" Your Password :{password}")

elif choice == "hard" :
#Hard
    shuffled_password =""
    password_list = list(password)
    random.shuffle(password_list)
    for char in password_list :
        shuffled_password += char
    print(f" Your Password :{shuffled_password}")

else :
    print("You have typed invalid choice!")


