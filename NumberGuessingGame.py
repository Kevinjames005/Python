import random

logo = r'''
  /$$$$$$                                               /$$$$$$$$ /$$                
 /$$__  $$                                             |__  $$__/| $$                
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/
 /$$   /$$                         /$$                                               
| $$$ | $$                        | $$                                               
| $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$                      
| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$                     
| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/                     
| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$                           
| $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$                           
|__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/                           
'''

print(logo)
random_number = random.randint(1,100)
print("Welcome to the Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
def easy():
    life = 10
    game = False
    while not game and life > 0 :
        print(f"You have {life} attempts to guess the number")
        guess = int(input("Make a guess : "))
        if guess == random_number :
            print(f"You got it ! The answer was {random_number}")
            game = True
        else :
            if guess < random_number:
                print("Too Low.")
            else :
                print("Too high")
        life -= 1
    if life == 0 and not game:
        print("You've run out of Guesses.")

def hard():
    life = 5
    game = False
    while not game and life > 0 :
        print(f"You have {life} attempts to guess the number")
        guess = int(input("Make a guess : "))
        if guess == random_number :
            print(f"You got it ! The answer was {random_number}")
            game = True
        else :
            if guess < random_number:
                print("Too Low.")
            else :
                print("Too high")
        life -= 1
    if life == 0 and not game :
        print("You've run out of Guesses.")

if level == "hard" :
    hard()
elif level == "easy":
    easy()
else :
    print("Invalid Option!.")