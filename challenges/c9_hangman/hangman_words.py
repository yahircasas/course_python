# Importamos la biblioteca random para seleccionar palabras al azar
import random

# Lista de palabras para el juego
palabras = [
    'probabilidad', 'valor esperado', 'seguro', 'contingente', 'plazo',
    'varianza', 'prima', 'mortalidad', 'gompertz', 'makeham',
    'exponencial', 'recursión', 'tasa', 'descuento', 'interés',
    'anualidad', 'pago', 'beneficio', 'vida entera', 'vida entera diferida',
    'endoso puro', 'seguro de vida entera', 'fuerza de interés', 'tabla de vida',
    'fuerza constante de mortalidad', 'valor presente', 'distribución uniforme de fallecimientos',
    'discreto', 'continuo', 'prima neta', 'prima bruta', 'reserva',
    'reserva de gastos',
]

def elegir_palabra(palabras):
    """Selecciona una palabra al azar de la lista de palabras utilizando random.choice."""
    return random.choice(palabras).upper()

def ahorcado():
    palabra = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos = 6  # Número de intentos permitidos

    while intentos > 0:
        # Mostrar la palabra con letras adivinadas y guiones para letras no adivinadas
        palabra_mostrada = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
        print(f'Palabra: {palabra_mostrada}')

        if palabra_mostrada == palabra:
            print('¡Enhorabuena! Ha adivinado la palabra correctamente.')
            break

        print(f'Intentos restantes: {intentos}')
        print(f'Letras intentadas: {", ".join(letras_adivinadas)}')

        intento = input('Por favor, adivine una letra o la palabra completa: ').upper()

        if len(intento) == 1:  # Adivinar una letra
            if intento in letras_adivinadas:
                print('Usted ya ha intentado esa letra anteriormente.')
            elif intento in palabra:
                print('¡Acierto! La letra está en la palabra.')
                letras_adivinadas.append(intento)
            else:
                print('La letra no está en la palabra.')
                intentos -= 1
        else:  # Adivinar la palabra completa
            if intento == palabra:
                print('¡Felicidades! Ha adivinado la palabra correctamente.')
                break
            else:
                print('La palabra adivinada es incorrecta.')
                intentos -= 1

    else:
        print(f'Lo sentimos, se ha quedado sin intentos. La palabra era "{palabra}".')

if __name__ == "__main__":
    print('¡Bienvenido al juego del ahorcado!')
    ahorcado()
