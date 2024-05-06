# Generate and print the first 10 numbers in the Fibonacci sequence
## Utilizando recurción de funciones
# def fibonacci(n):
#     fib_secuencia=[0,1]
#     for i in range (2, n):
#         fib_secuencia.append(fib_secuencia[i-1] + fib_secuencia [i-2])
#     return fib_secuencia
#
# print(fibonacci(10))

## The same without functions recursion

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
