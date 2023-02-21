alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caesar Cipher!")
def encode_decode(msg, code, direction):
    if direction == "decode":
        code *= -1
    new_msg = ""
    for n in msg:
        position = (alphabet.index(n) + code) % 26
        new_letter = alphabet[position]
        new_msg += new_letter
    print(f"The encoded text is: {new_msg}.")
    run_again = input("Do you want to use the program again?").lower()
    if run_again == "yes":
        caesar_cipher()
    else:
        return

def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encode_decode(text, shift, direction)

caesar_cipher()

