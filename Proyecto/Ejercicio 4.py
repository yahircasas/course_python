'''
Por supuesto, aquí tienes una redacción:

Este programa funciona como una Calculadora de Prima de Seguro de Auto. Al iniciarlo, te pedirá que ingreses
información como tu edad, género, tipo de automóvil, historial de manejo y más. Basándose en estos datos, calculará
automáticamente la prima del seguro. Además, podrás elegir el periodo de pago que prefieras, ya sea mensual, anual,
semestral o trimestral. Una vez ingresados todos los datos y seleccionado el periodo de pago, el programa mostrará el
monto de la prima del seguro, adaptada a tus características y preferencias. Con esta herramienta, obtener una
estimación de tu prima de seguro de auto es rápido y sencillo.
'''

def calcular_prima_seguro(edad, genero, tipo_auto, historial_manejo, ubicacion, km_por_anio, caracteristicas_seguridad,
                          anio_fabricacion, nuevo_o_usado):
    # Precio base de la prima
    prima_base = 9000

    # Ajuste de prima basado en la edad del conductor
    if edad < 25:
        prima_base *= 2  # Aumento del 100% para conductores menores de 25 años

    # Ajuste de prima basado en el género del conductor
    if genero == "masculino":
        prima_base *= 1.5  # Primas más altas para conductores masculinos

    # Ajuste de prima basado en el tipo de automóvil
    if tipo_auto == "deportivo":
        prima_base *= 2  # Ajuste más alto para automóviles deportivos
    elif tipo_auto == "sedan":
        prima_base *= 1.5  # Ajuste más alto para sedanes

    # Ajuste de prima basado en el historial de manejo
    if historial_manejo == "bueno":
        prima_base *= 0.8  # Reducción del 20% para buen historial de manejo

    # Ajuste de prima basado en la ubicación
    if ubicacion == "ciudad":
        prima_base *= 1.4  # Ajuste para conductores en áreas urbanas

    # Ajuste de prima basado en la cantidad de kilómetros por año
    if km_por_anio > 20000:
        prima_base *= 1.5  # Ajuste más alto para conductores que conducen más de 20,000 km por año

    # Ajuste de prima basado en características de seguridad adicionales
    if caracteristicas_seguridad == "si":
        prima_base *= 0.9  # Reducción del 10% para automóviles con características de seguridad adicionales

    # Ajuste de prima basado en el año de fabricación y si es nuevo o usado
    if nuevo_o_usado == "nuevo" and anio_fabricacion > 2018:
        prima_base *= 0.9  # Reducción del 10% para automóviles nuevos fabricados después de 2018

    return prima_base


def calcular_prima_periodica(prima, periodo):
    if periodo == "mensual":
        return round(prima / 12, 2)
    elif periodo == "anual":
        return round(prima, 2)
    elif periodo == "semestral":
        return round(prima * 2, 2)
    elif periodo == "trimestral":
        return round(prima * 4 / 3, 2)
    else:
        return "Periodo no válido"


def main():
    print("Calculadora de Prima de Seguro de Auto")
    print("--------------------------------------")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (masculino/femenino): ").lower()
    tipo_auto = input("Ingrese el tipo de su automóvil (deportivo/sedan/camioneta/compacto/furgoneta/normal): ").lower()
    historial_manejo = input("Ingrese su historial de manejo (bueno/malo): ").lower()
    ubicacion = input("Ingrese su ubicación (ciudad/campo): ").lower()
    km_por_anio = int(input("Ingrese la cantidad de kilómetros que planea conducir por año: "))
    caracteristicas_seguridad = input("¿Su automóvil tiene características de seguridad adicionales? (si/no): ").lower()
    anio_fabricacion = int(input("Ingrese el año de fabricación de su automóvil: "))
    nuevo_o_usado = input("¿Su automóvil es nuevo o usado? (nuevo/usado): ").lower()
    periodo = input("¿En qué periodo desea pagar la prima? (mensual/anual/semestral/trimestral): ").lower()

    prima_base = calcular_prima_seguro(edad, genero, tipo_auto, historial_manejo, ubicacion, km_por_anio,
                                       caracteristicas_seguridad, anio_fabricacion, nuevo_o_usado)
    prima_periodica = calcular_prima_periodica(prima_base, periodo)

    print("\nLa prima de su seguro de auto es:", prima_periodica, "en", periodo)


if __name__ == "__main__":
    main()
