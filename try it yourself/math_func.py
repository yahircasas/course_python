'''
Hazme esto en python
1) Create the function in python
2)Create a list with 10,000 random numbers from a Normal distribution with miu=2 y varianza = 5.
3) Evaluate teh function with the ramndom integers
4) Print out the results

f(n)= n/3 si n es mayor o igual a cero y es -(n+5)/6 si n es menor a cero
g(x)= raiz de x si x es menor estricto a cero, es 4cos(2*pi*x) si x es mayor o igual a 0 y x es menor estricto a 1 y x*log con base 2(euler a la x * tangente hiperbolica de x) si x es mayor o igual a 1
 pero por ejemplo quiero que me des 10000 resultados para random numbers from normal, 10000 de la evaluation in f and 10,000 in evaluation in g
'''
import numpy as np
import math

# Definir la función f(n)
def f(n):
    if n >= 0:
        return n / 3
    else:
        return -(n + 5) / 6

# Definir la función g(x)
def g(x):
    if x < 0:
        return math.sqrt(-x)
    elif 0 <= x < 1:
        return 4 * math.cos(2 * math.pi * x)
    else:
        return x * math.log(math.exp(x) * math.tanh(x), 2)

# Crear una lista con 10,000 números aleatorios de una distribución normal con miu=2 y varianza=5
mu = 2
sigma = math.sqrt(5)  # La desviación estándar es la raíz cuadrada de la varianza
random_numbers = np.random.normal(mu, sigma, 10000)

# Evaluar la función f(n) con los números aleatorios
results_f = [f(n) for n in random_numbers]

# Evaluar la función g(x) con los números aleatorios
results_g = [g(x) for x in random_numbers]

# Imprimir los números aleatorios generados
print("Números aleatorios de la distribución normal:")
print(random_numbers)

# Imprimir los resultados de la función f(n)
print("\nResultados de f(n):")
print(results_f)

# Imprimir los resultados de la función g(x)
print("\nResultados de g(x):")
print(results_g)

