# Manera de utilizar los keywords arguments, todos así o todos posicionales.
# ra = range(1,10,2) # únicamente posicional
# ra = range(start=1, end=10, 2) # La función integrada está definida únicamente posicional

# Definiendo una función con argumentos solo posicionales.
def func1(value1, value2, value3, /):
    print(value1 / value2 + value3)

func1(1, 2, 3)

# Posicional o por palabra clave con una función integrada
# Complex va a permitir posicional y palabras clave argumentos
com = complex(imag=5, real=1)
com2 = complex(real=1, imag=5)
com3 = complex(5, 4)
com4 = complex(10)
print(com)
print(com2)
print(com3)
print(com4)

# Definiendo una función con argumentos posicionales o por palabra clave
def func2(r, i=0):
    print(f'{r}+{i}j')

func2(i=4, r=8)
func2(8, 4)

# Solo palabra clave
def func3(pos1, *, live, student=''):
    print(live + student + str(pos1))

func3(5, live='True', student='jake')

# Función con una mezcla de posicionales, posicional o palabra clave, y solo palabra clave
def some(obs, k_or_guess, my_iter='29', /, thresh='1e-05', check_finity='True', *, seed='None'):
    print(obs + k_or_guess + my_iter + thresh + check_finity + seed)

some('hola', 'adios', seed='example')
