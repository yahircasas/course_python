# Write a program to find and print all prime numbers between 1 and 100

for num in range (1,1000000):
    div = 0
    for _ in range (1,101):
        if num % _ == 0:
            div += 1
    if div <= 2:
        print(num, end= ' ')
