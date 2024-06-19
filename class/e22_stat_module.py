# Read the documentation and use the functions you want, like the previous exercise

import statistics as estadisticas

# Media ponderada
def media_ponderada(datos, pesos):
    if len(datos) != len(pesos):
        raise ValueError("Los datos y los pesos deben tener la misma longitud.")

    media_ponderada_valor = sum(x * w for x, w in zip(datos, pesos)) / sum(pesos)
    return media_ponderada_valor

# Correlación entre dos conjuntos de datos
def calcular_correlacion(datos1, datos2):
    correlacion = estadisticas.correlation(datos1, datos2)
    return correlacion

if __name__ == "__main__":
    datos = [32, 45, 28, 19, 37, 30, 24]
    pesos = [0.1, 0.2, 0.1, 0.15, 0.2, 0.1, 0.15]
    datos2 = [24, 32, 18, 21, 30, 25, 28]

    # Calcular la media ponderada
    media_ponderada_valor = media_ponderada(datos, pesos)
    print("Media ponderada de los datos:", media_ponderada_valor)

    # Calcular la correlación entre los dos conjuntos de datos
    correlacion_valor = calcular_correlacion(datos, datos2)
    print("Correlación entre los dos conjuntos de datos:", correlacion_valor)
