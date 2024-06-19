# Make a function called 'my_split' that imitates the behavior of split() method
# But this function takes the string as a parameter, and by default the cut is a space, and return a list with the words
def my_split(cadena, separador=' '):
    palabras = []
    palabra_actual = ''

    for caracter in cadena:
        if caracter == separador:
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual = ''
        else:
            palabra_actual += caracter

    if palabra_actual:
        palabras.append(palabra_actual)

    return palabras

texto1 = "Las matemáticas son abstractas"
resultado = my_split(texto1)
print(resultado)

texto2 = "Las, matemática, son, abstractas"
resultado_otro = my_split(texto2, separador=',')
print(resultado_otro)
