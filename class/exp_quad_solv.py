"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""

# def calcular_raices(a, b, c):
#     discriminante = b**2 - 4*a*c
#     raiz1 = (-b + discriminante**0.5) / (2*a)
#     raiz2 = (-b - discriminante**0.5) / (2*a)
#     return raiz1, raiz2
#
# a, b, c = 2, 2, 0
# raices = calcular_raices(a, b, c)
# print("Las raíces de la ecuación son:", raices)

quad= lambda a, b, c: ((-b + pow(pow(b, 2) - 4 * a * c, 1/2)) / (2 * a), (-b - pow(pow(b, 2) - 4 * a * c, 1/2)) / (2 * a))
print(quad(2,2,0))
