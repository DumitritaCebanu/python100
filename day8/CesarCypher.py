# positional arguments
def greetings(name, location):
    print(f"Hello {name}")
    print(f"What a nice weather in {location}")


# keyword arguments
def greeting(name="Ina", location="Chisinau"):
    print(f"Hello {name}")
    print(f"What a nice weather in {location}")


# greetings("Dumi", "Timisoara")
# greeting()


# Prime numbers
def check_prime_numbers(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


# check_prime_numbers(12)

# Cesar Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("type the shift number:\n"))
shift = shift % 26


# Create a function called 'encrypt' that takes the 'text' and 'shift' as input
# sift each letter of the text forward in the alphabet by the shift amount and print
# the encrypted text
def cesar(message=text, shift_nr=shift, choice=direction):
    encrypt_message = ""
    decrypt_message = ""
    for letter in message:
        if choice == "encode":
            new_position = alphabet.index(letter) + shift_nr
            new_letter = alphabet[new_position]
            encrypt_message += new_letter
        elif choice == "decode":
            new_position = alphabet.index(letter) - shift_nr
            new_letter = alphabet[new_position]
            decrypt_message += new_letter
        else:
            print("invalid choice")
    if choice == "encode":
        print("Encoded message:", encrypt_message)
    elif choice == "decode":
        print("Decoded message:", decrypt_message)


cesar()
