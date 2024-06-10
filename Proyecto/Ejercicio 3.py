'''
Escribir un algoritmo que calcule los números primos de 0 a
100 utilizando el llamado método de la criba de Eratóstenes.
Este método consiste en definir e inicializar con todos sus
elementos a True un vector de 100 elementos binarios e ir
“tachando” (pasando a False) en pasadas sucesivas todos los
múltiplos de los números primos (2, 3, 5, 7...) hasta obtener
sólo los números primos.
'''
def criba_de_eratostenes(n):
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  #  0 y 1 no son primos

    # Iterar desde 2 hasta la raíz cuadrada de n
    p = 2
    while p * p <= n:
        if es_primo[p]:
            # Marcar todos los múltiplos de p como no primos
            for i in range(p * p, n + 1, p):
                es_primo[i] = False
        p += 1

    # Recoger todos los números primos en una lista
    primos = [num for num, primo in enumerate(es_primo) if primo]
    return primos

# Calcular los números primos de 0 a 100
primos_hasta_100 = criba_de_eratostenes(100)
print(primos_hasta_100)
