## A word is a polindrome if it is identical forward and backward. For example, anna, civic, level and hannah are all
# examples of palindromic words. Write a program that treads a word from the user to determine whether it is a
# palindrome. Display the result, including a meaning output message.
#
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1] # Return a bulean value.

def main():
    user_word = input("Ingresa una palabra para verificar si es un palíndromo: ")
    if is_palindrome(user_word):
        print("¡La palabra '{}' es un palíndromo!".format(user_word))
    else:
        print("La palabra '{}' no es un palíndromo.".format(user_word))

if __name__ == "__main__":
    main()

# def check_palindrome(word):
#     # Convertimos la palabra a minúsculas para hacer la comparación insensible a mayúsculas
#     word = word.lower()
#     # Comparamos la palabra original con su versión invertida
#     if word == word[::-1]:
#         return f"¡La palabra '{word}' es un palíndromo!"
#     else:
#         return f"La palabra '{word}' no es un palíndromo."
#
# def main():
#     user_word = input("Ingresa una palabra para verificar si es un palíndromo: ")
#     result = check_palindrome(user_word)
#     print(result)
#
# if __name__ == "__main__":
#     main()


# def palindrone(word):
#     tam = len(word)
#     ad = 0
#     at = -1
#     while ad <= tam-1 and at >= -tam:
#         if word[ad] == word[at]:
#             ad += 1
#             at -= 1
#         else:
#             print('Esta palabra no es un Palindrono :')
#             break
#     if ad > tam-1 or at < -tam:
#         print('Esta palabra es un Palindrono :)')
#
# palindrone(input('Inserte una palabra:'))


# Teacher
# word = input("Enter a word to verify if it is a palindrome: ")
# word2 = ""
# word_List = list(word)
# word_List.reverse()
# for char in word_List:
#     word2 = word2 + char
# if word == word2:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
