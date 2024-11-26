import random

hangman_lives = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']

word_list = ["ant", "avocardo", "baboon", "backpack", "badger", "ball", "basket", "bat", "bear", "beaver", "bed", "book", "bottle", "bridge", "camel", "camera", "candle", "car", "cat", "ceiling", "chair", "clam", "clock", "cloud", "cobra", "coffee", "computer", "cougar", "coyote", "crow", "cup", "deer", "desert", "dog", "donkey", "door", "duck", "eagle", "fan", "ferret", "flower", "forest", "fox", "frog", "garden", "glasses", "goat", "goose", "grass", "guitar", "hat", "hawk", "house", "jacket", "keyboard", "kitchen", "lamp", "lion", "lizard", "llama", "maturity", "mirror", "mole", "mountain", "notebook", "ocean", "painting", "paper", "pencil", "phone", "piano", "plane", "rat", "raven", "rhino", "river", "road", "shark", "sheep", "shoe", "sky", "soap", "spider", "stone", "stove", "table", "telescope", "television", "toad", "towel", "train", "tree", "turkey", "turtle", "umbrella", "wallet", "wheel", "window", "wolf", "wombat", "zebra" ]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
life = 0

for i in chosen_word :
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over :
    print(f"**************************************** {life}/6 Lives Left****************************************")
    guess = input("Guess a letter:").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess :
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters :
            display += letter
        else :
            display += "_"
    if guess in correct_letters :
        print("You have already guessed the letter")
    if guess not in chosen_word :
        life += 1
        print(f"You gussed {guess} , and you have lost a life")
    print(display)
    print(hangman_lives[life])

    if life == 6 :
        game_over = True
        print("You Lose")
        print(f"The word was {chosen_word}")
    if display == chosen_word :
        game_over = True
        print("You Win")

        
