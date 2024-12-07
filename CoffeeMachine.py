MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money_in_machine = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report() :
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g")
    print(f"Money : ${money_in_machine}")

def check_resources_latte():
    if MENU["latte"]["ingredients"]["water"] <= resources["water"] :
        if MENU["latte"]["ingredients"]["milk"] <= resources["milk"] :
            if MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else :
            print("Sorry there is not enough milk.")
            return False
    else :
        print("Sorry there is not enough water.")
        return False
def check_resources_espresso():
    if MENU["espresso"]["ingredients"]["water"] <= resources["water"] :
        if MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            print("Sorry there is not enough coffee.")
            return False
    else :
        print("Sorry there is not enough water.")
        return False

def check_resources_cappuccino():
    if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] :
        if MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"] :
            if MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else :
            print("Sorry there is not enough milk.")
            return False
    else :
        print("Sorry there is not enough water.")
        return False
def calculate_money():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    no_of_quarters = int(input("Quarters :"))
    no_of_dimes = int(input("Dimes :"))
    no_of_nickles = int(input("Nickles :"))
    no_of_pennies = int(input("Pennies :"))
    total = (quarters * no_of_quarters) + (dimes * no_of_dimes) + (nickles * no_of_nickles) + (pennies * no_of_pennies)
    return total


def not_enough_money():
    print("Sorry that's not enough money. Money refunded.")

refund = 0

Machine_ON_or_OFF = True
while Machine_ON_or_OFF :
    order = input("What would you like : (espresso/latte/cappuccino) : ").lower()
    if order == "report" :
        report()
    elif order == "latte" :
        if check_resources_latte() :
            print("You can insert coins:")
            money = calculate_money()
            if money >= MENU["latte"]["cost"] :
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                money_in_machine += MENU["latte"]["cost"]
                print("Your latte is ready: 🍵 Enjoy!")
                if money > MENU["latte"]["cost"] :
                    refund = float(money) - float(MENU["latte"]["cost"])
                    refund = round(refund,2)
                    print(f"Here is your change: ${refund}")
            else :
                not_enough_money()
    elif order == "espresso":
        if check_resources_espresso():
            print("You can insert coins:")
            money = calculate_money()
            if money >= MENU["espresso"]["cost"]:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                money_in_machine += MENU["espresso"]["cost"]
                print("Your espresso is ready: ☕ Enjoy!")
                if money > MENU["espresso"]["cost"]:
                    refund = float(money) - float(MENU["espresso"]["cost"])
                    refund = round(refund, 2)
                    print(f"Here is your change: ${refund}")
            else:
                not_enough_money()
    elif order == "cappuccino":
        if check_resources_cappuccino():
            print("You can insert coins:")
            money = calculate_money()
            if money >= MENU["cappuccino"]["cost"]:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                money_in_machine += MENU["cappuccino"]["cost"]
                print("Your cappuccino is ready: ☕︎ Enjoy!")
                if money > MENU["cappuccino"]["cost"]:
                    refund = float(money) - float(MENU["cappuccino"]["cost"])
                    refund = round(refund, 2)
                    print(f"Here is your change: ${refund}")
            else:
                not_enough_money()
    elif order == "refill" :
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    elif order == "off" :
        print("Turning off......!")
        Machine_ON_or_OFF = False
    else :
        print("Invalid Command")
