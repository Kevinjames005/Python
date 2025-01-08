import pandas
#TODO 1. Create a dictionary
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
while True:
    try:
        nato_words_list =[nato_dict[letter] for letter in word]
        print(nato_words_list)
        break
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        word = input("Enter a word").upper()




