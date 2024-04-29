"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""
number = int(input('Digite un número:'))
while True:
    if number % 2 == 0:
        num = number/2
        print(num)
        if num % 2 == 0:
            num = num/2
            print(num)
        break
    else:
        number = number * 3 + 1
        continue