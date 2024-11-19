import random

paper ='''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose ? , Type 0 for Rock , 1 for Scissors and 2 for Paper\n"))

if choice == 0 :
    print(rock)
elif choice == 1 :
    print(scissors)
elif choice == 2 :
    print(paper)
else :
    print("Invalid option")

print("Computer Chose:")

computer_choice = random.randint(0,2)
if computer_choice == 0 :
    print(rock)
elif computer_choice == 1 :
    print(scissors)
elif computer_choice == 2 :
    print(paper)
else :
    print("Invalid option")

if (choice == 0 and computer_choice==2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1) :
    print("You lose")
elif (choice == 2 and computer_choice==0) or (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) :
    print("You win")
elif choice == computer_choice :
    print("Draw")
else :
    print("You have given a invalid Option , You Lose!")


