print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

''')

print("Welcome to the Treasure Island.")
print("Your mission is to find out the treasure")
direction = input("You are at a cross road. Where do you want to go? \n\t type left or right. ").lower()
if direction == "left" :
    print("You have come to a lake. There is a island in the middle of the lake.")
    cross_the_lake = input("You can either wait for a boat or swim across the lake. Type wait or swim. ").lower()
    if cross_the_lake == "wait" :
        print("you arrived at the island unharmed. There is a house with 3 doors.")
        colour = input("One red , one yellow and one blue. Which colour do you choose. ").lower()
        if colour == "yellow" :
            print("Booyah ! You found the treasure.")
        elif colour == "red" :
            print("You have gotten into a room full of fire.You are dead.")
            print("GAMEOVER!!")
        elif colour == "blue" :
            print("You have gotten into a room full of Gorillas and you are beaten to death")
            print("GAMEOVER!!")
        else :
            print("Invalid choice.")
    elif cross_the_lake == "swim" :
        print("You have encountered a serpent in the lake and it killed you.")
        print("GAMEOVER!!")
elif direction == "right" :
    print("You fell into a hole. GAMEOVER!!")
else :
    print("Invalid choice.")
