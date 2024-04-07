"""
In this exercise, you will create a program that reads a letter of the alphabet from the user.
If the user enters a,e,i,o or u then your program should display a message indicating that the entered letter is a vowel
If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y
is a consonant. Otherwise, your program should display a message indicating that the letter is a consonant.
"""
# Prompt the user to enter a letter of the alphabet and convert it to lowercase
letter = input("Enter a letter of the alphabet: ").lower()

# Check if the entered letter is a vowel
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The entered letter is a vowel.")
# Check if the entered letter is 'y'
elif letter == 'y':
    print("Sometimes 'y' is a vowel, and sometimes 'y' is a consonant.")
# If the entered letter is not a vowel or 'y', it's a consonant
else:
    print("The entered letter is a consonant.")
