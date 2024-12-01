logo = '''
 _____________________
|  _________________  |
| | CALCULATOR   0. | |
| |_________________| |     
|  ___ ___ ___   ___  |              _            _       _ 
| | 7 | 8 | 9 | | + | |             | |          | |     | | 
| |___|___|___| |___| |     ___ __ _| | ___ _   _| | __ _| |_ ___  _ __  
| | 4 | 5 | 6 | | - | |    / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__|
| |___|___|___| |___| |   | (_| (_| | | (__| |_| | | (_| | || (_) | | 
| | 1 | 2 | 3 | | x | |    \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

def add(n1, n2) :
    return n1 + n2

def subtract(n1 , n2) :
    return n1 - n2

def multiply (n1 , n2):
    return n1 * n2

def division(n1 , n2):
    return n1 / n2

calc_dictionary = {"+" : add ,
                   "-" : subtract ,
                   "*" : multiply ,
                   "/" : division
}

is_continue = True
print(logo)
first_number = float(input("Enter the first number: "))
while is_continue :
    operation = input("Choose an operation:\n+\n-\n*\n/\n")
    next_number = float(input("Enter the next number: "))
    result = 0

    if operation == "+":
        result = calc_dictionary["+"](first_number , next_number)
        print(f"{first_number} + {next_number} = {result}")
    elif operation == "-" :
        result = calc_dictionary["-"](first_number, next_number)
        print(f"{first_number} - {next_number} = {result}")
    elif operation == "*" :
        result = calc_dictionary["*"](first_number, next_number)
        print(f"{first_number} * {next_number} = {result}")
    elif operation == "/" :
        result = calc_dictionary["/"](first_number, next_number)
        print(f"{first_number} / {next_number} = {result}")
    else :
        print("Invalid option")

    yes_or_no = input(f"Type yes if you want to do an operation with the {result} , else type no :").lower()

    if yes_or_no == "yes":
        first_number = result
    elif yes_or_no == "no":
        print("\n"*100)
        print(logo)
        first_number = float(input("Enter the first number: "))


