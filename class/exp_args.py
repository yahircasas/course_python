"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""
# def sum_args (*numbers):
#     return sum(numbers)
# a=sum_args(2,3,4,5)
# print(a)

"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""
# def concact_strings(*datails):
#     return ''.join(datails)
# a=concact_strings('Shan', 'Rossy', 'yahir')
# print(a)


"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""
def calcular_gastos(nombre, ingreso_mensual, gastos_variables, **gastos_fijos):
    # Se suman los gastos fijos
    total_gastos_fijos = sum(gastos_fijos.values())
    # Total de gastos =(fijos + variables)
    total_gastos = total_gastos_fijos + gastos_variables
    saldo_restante = ingreso_mensual - total_gastos

    print(f"Nombre: {nombre}")
    print(f"Ingreso Mensual: ${ingreso_mensual:.2f}")
    print(f"Gastos Variables: ${gastos_variables:.2f}")
    print("Gastos Fijos:")
    for gasto, monto in gastos_fijos.items():
        print(f"  {gasto}: ${monto:.2f}")
    print(f"Total Gastos Fijos: ${total_gastos_fijos:.2f}")
    print(f"Total Gastos: ${total_gastos:.2f}")
    print(f"Saldo Restante: ${saldo_restante:.2f}")

calcular_gastos("Yahir Casas", 5000, 1750, renta=1600, servicios=600, internet=450, seguro=600)

