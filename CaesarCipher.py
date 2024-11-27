alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''

 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

''')


def caesar(direction_value):
    if direction_value == "encode":
        encrypt(original_text = text , shift_amount = shift)
    elif direction_value == "decode" :
        decrypt(cipher_text = text , shift_amount = shift)
    else :
        print("Invalid option !.")

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabets :
            shifted_position = alphabets.index(letter) + shift_amount
            if shifted_position > 25 :
                new_shift_position = shifted_position - 26
                encrypted_text += alphabets[new_shift_position]
            else :
                encrypted_text += alphabets[shifted_position]
        else :
            encrypted_text += letter
    print(f"The encrypted text is : {encrypted_text}.")

def decrypt(cipher_text , shift_amount):
    decoded_text = ""
    for letter in cipher_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) - shift_amount
            if shifted_position < 0 :
                new_shift_position = 26 + shifted_position
                decoded_text += alphabets[new_shift_position]
            else :
                decoded_text += alphabets[shifted_position]
        else :
            decoded_text += letter

    print(f"The decoded text is : {decoded_text}.")

do_it_again = False
while not do_it_again :
    direction = input("Type 'encode' to Encrypt and 'decode' Decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction_value = direction)
    do_it_again = input("Type Yes , if you want to continue and No , if you don't want to continue.\n").lower()
    if do_it_again == "yes" :
        do_it_again = False
    elif do_it_again == "no" :
        do_it_again = True
    else :
        print("Invalid Option")
