#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as s_letter:
    letter = s_letter.read()

with open("./Input/Names/invited_names.txt") as each_name:
    names = each_name.readlines()

#for each name in invited_names.txt
for name in names:
    name = name.strip("\n")

    # Replace the [name] placeholder with the actual name.
    final_letter = letter.replace("[name]" , f"{name}")

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{name}.txt", mode= "w") as send_letter:
        send_letter.write(final_letter)
