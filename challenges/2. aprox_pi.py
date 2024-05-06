"""
Use Nilakantha's series to approximate pi.
Show 15 approximations of pi.The first approx should be the first term of the series, the second approx the second term
and so on
pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...

https://i1.wp.com/www.glc.us.es/~jalonso/exercitium/wp-content/uploads/2017/02/Calculo_de_pi_mediante_la_serie_de_Nilakantha.png?resize=571%2C83
"""

# def nilakantha_series(n):
#     pi_approx = 3.0
#     sign = 1.0
#
#     for i in range(1, n + 1):
#         term = 4.0 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
#         pi_approx += sign * term
#         sign *= -1
#
#     return pi_approx
#
# def main():
#     print("Approximations of pi using Nilakantha's series:")
#     for i in range(1, 16):
#         approximation = nilakantha_series(i)
#         print(f"Term {i}: {approximation}")
#
# if __name__ == "__main__":
#     main()


def nilakantha_series(n):
    pi_approx = 3.0
    sign = 1.0

    for i in range(1, n + 1):
        term = 4.0 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
        pi_approx += sign * term
        sign *= -1

    return pi_approx

def main():
    n = int(input("Enter the number of approximations of pi you want to see: "))
    print("Approximations of pi using Nilakantha's series:")
    for i in range(1, n + 1):
        approximation = nilakantha_series(i)
        print(f"Aprox {i}: {approximation}")

if __name__ == "__main__":
    main()

