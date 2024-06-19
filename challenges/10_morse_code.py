import winsound
from time import sleep

# Definición del diccionario de código Morse
MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                   'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                   'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                   'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                   'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                   'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
                   '4':'....-', '5':'.....', '6':'-....', '7':'--...',
                   '8':'---..', '9':'----.', '0':'-----', ', ':'--..--',
                   '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                   '(':'-.--.', ')':'-.--.-'}

def texto_a_morse(texto):
    codigo_morse = []
    for caracter in texto.upper():
        if caracter in MORSE_CODE_DICT:
            codigo_morse.append(MORSE_CODE_DICT[caracter])
        elif caracter == ' ':
            codigo_morse.append('/')
    return ' '.join(codigo_morse)

def reproducir_codigo_morse(codigo_morse):
    for simbolo in codigo_morse:
        if simbolo == '.':
            winsound.Beep(1000, 200)  # Beep para el punto (.)
        elif simbolo == '-':
            winsound.Beep(1000, 400)  # Beep para el guion (-)
        elif simbolo == '/':
            sleep(0.5)  # Pausa entre cada palabra
        sleep(0.2)  # Pausa entre símbolos dentro de la misma letra

if __name__ == '__main__':
    texto = input("Ingresa el texto para convertir a código Morse: ")
    codigo_morse = texto_a_morse(texto)
    print(f"Código Morse: {codigo_morse}")
    reproducir_codigo_morse(codigo_morse.split())
