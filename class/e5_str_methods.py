full_name = 'satoshi nakamoto'  # capitalize(), title()
print(full_name.capitalize())  # convierte la primera letra en mayúscula.
print(full_name.title())  # convierte la primera letra de cada palabra en mayúscula.

state = 'mississippi'  # count('ss'), count('pp'), count('ppp')
print(state.count('ss'))  # cuenta cuántas veces aparece 'ss'.
print(state.count('pp'))  # cuenta cuántas veces aparece 'pp'.
print(state.count('ppp'))  # cuenta cuántas veces aparece 'ppp'.

url = 'www.python.orgw'  # startswith('ww'), endswith('g'), endswith('.py'), strip('w'), rstrip('w'), lstrip('w')
print(url.startswith('ww'))  # verifica si la URL comienza con 'ww'.
print(url.endswith('g'))   # verifica si la URL termina con 'g'.
print(url.endswith('.py'))  # verifica si la URL termina con '.py'.
print(url.strip('w'))   # elimica caracteres 'w' del inicio y final de la URL.
print(url.rstrip('w'))  # elimina caracteres 'w' del final de la URL.
print(url.lstrip('w'))  # elimina caracteres 'w' del inicio de la URL.

sentence = 'I saw a saw saw'  # find('saw'), rfind('saw'), find('jeje'), index('saw'), rindex('saw'), index('jeje')
print(sentence.find('saw'))  # encuentra la primera aparición de 'saw'
print(sentence. rfind('saw'))  # encuentra la última aparición de 'saw'
print(sentence.find('jeje'))  # Busca el carácter 'jeje' en la oración
print(sentence.index('saw'))  # obtiene el índice de la primera ocurrencia de 'saw'
print(sentence.rindex('saw'))  # obtiene el índice de la última ocurrencia de 'saw'

func = '5tAn(x)'  # upper(), lower(),
print(func.upper())  # convierte todos los caracteres a mayúsculas.
print(func.lower())  # convierte todos los caracteres a minúsculas.

swap = 'AAAhhHaAhh'  # swapcase()
print(swap.swapcase())  # intercambia entre mayúsculas y minúsculas.

song = 'LUMBERJACK'  # isupper(), islower()
print(song.isupper())  # verifica si todos los caracteres están en mayúsculas.
print(song.islower())  # verifica si todos los caracteres están en minúsculas.

string = "I'm bad in Python"  # replace('bad', 'good')
print(string.replace('bad', 'good'))  # reemplaza a 'bad' por 'good'.

e = '2.71828'  # isalnum(), isalpha(), isdecimal(), isdigit(), isnumeric()
print(e.isalnum())  # verifica si todos los caracteres son alfanuméricos.
print(e.isalpha())  # verifica si todos los caracteres son alfabéticos.
print(e.isdecimal())  # verifica si todos los caracteres son decimales.
print(e.isdigit())  # verifica si todos los caracteres son dígitos.
print(e.isnumeric())  # verifica si todos los caracteres son numéricos.

num = 18055  # isalnum(), isalpha(), isdecimal(), isdigit(), isnumeric()
print(str(num).isalnum())  # verifica si todos los caracteres en la representación de cadena son alfanuméricos.
print(str(num).isalpha())  # verifica si todos los caracteres en la representación de cadena son alfabéticos.
print(str(num).isdigit())  # verifica si todos los caracteres en la representación de cadena son dígitos.
print(str(num).isdigit())  # verifica si todos los caracteres en la representación de cadena son dígitos.
print(str(num).isnumeric())  # verifica si todos los caracteres en la representación de cadena son numéricos.

# Create a string where the istitle() method returns True
tittle = 'Las Matematicas Son Importantes'
print(tittle.istitle())

# Create a string where the isspace() method returns True
space = '    '
print(space.isspace())

# Create a string where you can use removeprefix() and removesuffix(). Hint: use a URL
url_2= 'www.python.org'
print(url_2.removeprefix('www').removesuffix('w'))

# Create a valid object where you can use split() method
fruits = 'apple,grape,kiwi,watermelon'
print(fruits.split(','))
