"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
    Take both people's names and check for the number of times the letters in the word TRUE occur.
    Then check for the number of times the letters in the word LOVE occur.
    Then combine these numbers to make a 2 digits number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. E.g.:
"Your score is *z*."
"""


def calcular_puntaje_amor(nombre1, nombre2):
    nombres_combinados = nombre1.lower() + nombre2.lower()

    true_count = nombres_combinados.count('t') + nombres_combinados.count('r') + nombres_combinados.count(
        'u') + nombres_combinados.count('e')
    love_count = nombres_combinados.count('l') + nombres_combinados.count('o') + nombres_combinados.count(
        'v') + nombres_combinados.count('e')

    puntaje_amor = int(str(true_count) + str(love_count))

    return puntaje_amor

def determinar_mensaje_puntaje(puntaje):
    if puntaje < 10 or puntaje > 90:
        return f"Tu puntaje es {puntaje}, van juntos como la coca y los mentos."
    elif 40 <= puntaje <= 50:
        return f"Tu puntaje es {puntaje}, están bien juntos."
    else:
        return f"Tu puntaje es {puntaje}."

nombre1 = input("Ingresa el nombre de la primera persona: ")
nombre2 = input("Ingresa el nombre de la segunda persona: ")
puntaje = calcular_puntaje_amor(nombre1, nombre2)
mensaje = determinar_mensaje_puntaje(puntaje)
print(mensaje)
