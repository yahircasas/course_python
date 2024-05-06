"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9 / 5) + 32
#
#
# def main():
#     # Imprimir encabezados de la tabla
#     print("Celsius\tFahrenheit")
#
#     # Generar la tabla de conversión
#     for celsius in range(0, 101, 10):
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(f"{celsius}\t{fahrenheit:.1f}")
#
#
# if __name__ == "__main__":
#     main()


from tabulate import tabulate

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    # Generar la tabla de conversión
    table = []
    for celsius in range(0, 101, 10):
        fahrenheit = celsius_to_fahrenheit(celsius)
        table.append([celsius, fahrenheit])

    # Imprimir la tabla
    headers = ["Celsius", "Fahrenheit"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
