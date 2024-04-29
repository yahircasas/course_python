# Generate and print the multiplication table (up to int) for a give number

number = int(input('Digite un número entre 1 y 10: '))
for number_1 in range (1,11):
    table = number_1*number
    print(f'{number} x {number_1} = {table}')