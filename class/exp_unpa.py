# Create a tuple with your first name, last name, and age. Then, unpack the tuple into three variables and print them.

datos_personales = ("Yahir", "Casas", 21)
nombre, apellido, edad = datos_personales

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)


"""
Initialize two variables a and b with any values. Swap their values using tuple unpacking and print the new values of
a and b.
"""
# Inicializar las variables
a = 10
b = 20

# Intercambiar valores usando desempaquetado de tupla
a, b = b, a

# Imprimir los nuevos valores de a y b
print("Nuevo valor de a:", a)
print("Nuevo valor de b:", b)


"""
Create a list with the first five prime numbers. Use extended unpacking to assign the first three primes to variables, 
and the rest to another variable. Print both sets of variables."""

# Primeros cinco números primos
primeros_primos = [2, 3, 5, 7, 11]
p1, p2, p3, *resto = primeros_primos
print("Primeros tres primos:", p1, p2, p3)
print("Resto de primos:", resto)

