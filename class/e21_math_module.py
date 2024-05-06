# Import the math module (as you want)
# import math as mt

####################################################################################################################
# Make the Poisson distribution. The user must enter the parameters. Then print out the result
# from scipy.stats import poisson
# lambda_par = float(input('Digite el valor de lambda: '))
# x_value = int(input('Digite el punto exacto de 5 al que evaluara la función: '))
# poisson_dtb =poisson(mu=lambda_par)
# density_value = poisson_dtb.pmf(x_value)
# print("El valor de la función de densidad en x =", x_value, "es:", density_value)

import math
# Obtener entrada del usuario para los valores de x y lambda
# x = int(input("Ingrese el valor de x: "))
# lmbda = float(input("Ingrese el valor de lambda (λ): "))
# # Calcular la función de densidad de Poisson
# result = (math.exp(-lmbda) * lmbda ** x) / math.factorial(x)
# # Imprimir el resultado
# print("La función de densidad de Poisson con x = {} y λ = {} es: {:.6f}".format(x, lmbda, result))

####################################################################################################################
# Make an iterable with some numbers to calculate the product of all those numbers

import math
# # Crear una lista de números
# numbers = [10, 2, 33, 44, 55]
# # Calcular el producto de todos los números en la lista usando math.prod()
# product = math.prod(numbers)
# # Imprimir el resultado
# print("El producto de los números es:", product)

####################################################################################################################
# From two iterables, calculate the sum of the product of values
import math
# # Dos iterables
# iterable1 = [4, 5, 7]
# iterable2 = [7, 9, 8]
# # Calcular la suma de los productos de los valores correspondientes
# result = sum(math.prod(pair) for pair in zip(iterable1, iterable2)) ##  combina los elementos de los iterables en pares y los empareja en tuplas
# # Imprimir el resultado
# print("La suma de los productos de los valores es:", result)


####################################################################################################################
# Calculate the GCD of two numbers that user gives (Greatest Common Divisor)
import math

# # Obtener entrada del usuario para los dos números
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
#
# # Calcular el máximo común divisor (GCD)
# gcd = math.gcd(num1, num2)
#
# # Imprimir el resultado
# print("El máximo común divisor de", num1, "y", num2, "es:", gcd)

####################################################################################################################
# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result
import math
#
# # Obtener entrada del usuario para los parámetros de la distribución binomial
# n = int(input("Ingrese el valor de n: "))  # Número total de ensayos
# x = int(input("Ingrese el valor de x: "))  # Número de éxitos deseados
# p = float(input("Ingrese el valor de p (probabilidad de éxito): "))  # Probabilidad de éxito en un solo ensayo
#
# # Calcular el coeficiente binomial (nCr)
# binomial_coefficient = math.comb(n, x)
#
# # Calcular la probabilidad de éxito y fracaso
# success_probability = math.pow(p, x)
# failure_probability = math.pow(1 - p, n - x)
#
# # Calcular la distribución binomial
# binomial_distribution = binomial_coefficient * success_probability * failure_probability
#
# # Imprimir el resultado
# print("La distribución binomial con n = {}, x = {} y p = {} es: {:.6f}".format(n, x, p, binomial_distribution))


####################################################################################################################
# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "

import math

# # Obtener entrada del usuario para un número flotante
# number = float(input("Ingrese un número flotante: "))
#
# # Calcular el techo del número dado
# ceiling = math.ceil(number)
#
# # Imprimir el resultado
# print("El techo de", number, "es", ceiling)


####################################################################################################################
# Choose two functions from the math documentation to make exercises like the previous

### Obtener el factorial de un numero decimal
# import math
#
# # Obtener entrada del usuario para un número flotante
# x = float(input("Ingrese un número flotante para calcular el factorial generalizado: "))
#
# # Calcular el factorial generalizado para el número dado
# generalized_factorial = math.gamma(x)
#
# # Imprimir el resultado
# print("El valor del factorial generalizado para", x, "es:", generalized_factorial)
#

# import math
#
# # Obtener entrada del usuario para un número flotante
# x = float(input("Ingrese un número flotante para calcular el coseno hiperbólico inverso: "))
#
# # Calcular el coseno hiperbólico inverso del número dado
# acosh_result = math.acosh(x)
#
# # Imprimir el resultado
# print("El coseno hiperbólico inverso de", x, "es:", acosh_result)
