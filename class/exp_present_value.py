"""
Write a lambda function to calculate the present value of an annuity-immediate given the interest rate,
number of periods, and periodic payment.
"""

# Función lambda para calcular el valor presente de una anualidad inmediata
calcular_valor_presente = lambda r, n, P: P * ((1 - (1 + r)**(-n)) / r)

tasa_interes = float(input("Ingresa la tasa de interés (en decimal, por ejemplo, 0.08 para 8%): "))
periodos = int(input("Ingresa el número de períodos: "))
pago_periodico = float(input("Ingresa el pago periódico: "))

# Calcular el valor presente de la anualidad inmediata utilizando la función lambda
valor_presente = calcular_valor_presente(tasa_interes, periodos, pago_periodico)

print(f"El valor presente de la anualidad inmediata es: {valor_presente:.2f}")

