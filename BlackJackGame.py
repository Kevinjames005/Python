import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_choice = []
computers_choice = []

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""




def blackjack() :
    print(logo)
    play = input("Do you want to play a game of blackjack, Type 'y' for yes and 'n' for no : ").lower()
    if play == "y" :
        for i in range(2):
            players_choice.append(random.choice(cards))
        sum_of_player = sum(players_choice)
        print(f"Your cards {players_choice} , current score = {sum_of_player}")

        for i in range(2):
            computers_choice.append(random.choice(cards))

        sum_of_computer = sum(computers_choice)
        print(f"Computers first card is : {computers_choice[0]}")

        get_another_card = input("Type 'y' to get another card and type 'n' to pass: ")

        if get_another_card == "n" :
            print(f"Your final hand : {players_choice} , Your score : {sum_of_player}")
            if sum_of_computer < 17:
                while sum_of_computer < 17:
                    computers_choice.append(random.choice(cards))
                    sum_of_computer = sum(computers_choice)
            print(f"Computer's final hand : {computers_choice} , Computers score : {sum_of_computer}")

        elif get_another_card == "y" :
            players_choice.append(random.choice(cards))
            computers_choice.append(random.choice(cards))
            sum_of_player = sum(players_choice)
            sum_of_computer = sum(computers_choice)
            if sum_of_computer < 17:
                while sum_of_computer < 17:
                    computers_choice.append(random.choice(cards))
                    sum_of_computer = sum(computers_choice)
            print(f"Your final hand : {players_choice} , Your score : {sum_of_player}")
            print(f"Computer's final hand : {computers_choice} , Computers score : {sum_of_computer}")



        #compare the values to find the winner
        if sum_of_player == 21:
            print("You Won")
        elif sum_of_player > 21 :
            print("You went overboard , you Lose")
        elif sum_of_player > sum_of_computer and sum_of_computer < 20 :
            print("You Won")
        elif sum_of_player == sum_of_computer :
            print("It's a draw.")
        elif sum_of_computer > 21 :
            print("You Won")
        else :
            print("You Lose.")
        play = input("Do you want to play a game of blackjack, Type 'y' for yes and 'n' for no : ").lower()
        print("\n"*100)
        computers_choice.clear()
        players_choice.clear()

        if play == "y":
            blackjack()

blackjack()
