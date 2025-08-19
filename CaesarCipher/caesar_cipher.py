alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        alphabet.index(letter)
        cipher_text += alphabet[(alphabet.index(letter) + shift_amount)]
    print(f"Encrypted text:  {cipher_text}")

def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text:
        alphabet.index(letter)
        original_text += alphabet[(alphabet.index(letter) - shift_amount)]
    print(f"Decrypted text:  {original_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid direction")
