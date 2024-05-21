"""
An integer, n, is said to be perfect when the sum of all the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number, then your
function will return True. Otherwise, it will return False. In addition, write a main
program that uses your function to identify and display all the perfect numbers
between 1 and 10,000.
"""


def es_numero_perfecto(n):

    if n <= 1:
        return False

    suma_divisores = sum(i for i in range(1, n) if n % i == 0)

    return suma_divisores == n

def main():

    user_input = int(input("Por favor, ingrese un número para verificar si es perfecto: "))

    if es_numero_perfecto(user_input):
        print("True")
    else:
        print("False")

    print("Números perfectos entre 1 y 10,000:")
    for num in range(1, 10001):
        if es_numero_perfecto(num):
            print(num)

if __name__ == "__main__":
    main()

