"""
One of the first known examples of encryption was used by Julius Caesar.
Read more about here: https://en.wikipedia.org/wiki/Caesar_cipher
Create a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and then display the shifted message.
Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift
values so that it can be used both to encode messages and decode messages.

# When you have done the code, try to decrypt the following:
ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch
"""

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(message, shift):
    result = ''
    for char in message:
        if char.isalpha():  # Check if character is an alphabet letter
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)  # Shift uppercase letters
            else:
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)  # Shift lowercase letters
            result += shifted_char
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def decrypt_caesar(message):
    possible_messages = []
    for shift in range(100):
        decrypted_message = caesar_cipher(message, -shift)
        possible_messages.append(decrypted_message)
    return possible_messages

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    mode = input("Enter 'encrypt' or 'decrypt': ")
    if mode.lower() == 'encrypt':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift amount: "))
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif mode.lower() == 'decrypt':
        message = input("Enter the message to decrypt: ")
        possible_messages = decrypt_caesar(message)
        print("Possible decrypted messages:")
        for i, decrypted_message in enumerate(possible_messages):
            print(f"Shift {i}: {decrypted_message}")

if __name__ == "__main__":
    main()
