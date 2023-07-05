import ascii_arts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text_e, shift_e):
    encoded_string = ""
    for n in range(0, len(text_e)):
        if text[n] in alphabet:
            encoded_string += alphabet[(alphabet.index(text_e[n]) + shift_e) % 26]
        else:
            encoded_string += text[n]
    print(f"The encoded text is '{encoded_string}'")


def decrypt(text_e, shift_e):
    decoded_string = ""
    for n in range(0, len(text_e)):
        if text[n] in alphabet:
            decoded_string += alphabet[(alphabet.index(text_e[n]) - shift_e) % 26]
        else:
            decoded_string += text[n]
    print(f"The encoded text is '{decoded_string}'")


print(ascii_arts.logo)

play = "yes"
while play == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Invalid input!")
    play = "no"
    while play != "yes":
        play = input("If you want to go again, enter 'yes', otherwise enter 'no': ")
        if play == "no":
            print("Good bye!")
            break
        elif play != "yes":
            print("Invalid input! Try again.")
