"""
Create a program that calculates the square root of a number with the Newton's method.
You should read the following: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
"""

def square_root_newton(number, tolerance=1e-10):
    if number < 0:
        raise ValueError("The number must be non-negative")

    guess = number / 2  # Aproximación inicial

    while True:
        new_guess = 0.5 * (guess + number / guess)  # Fórmula de Newton
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

def main():
    number = float(input("Enter a non-negative number to calculate its square root: "))
    square_root = square_root_newton(number)
    print("Square root of", number, "is:", square_root)

if __name__ == "__main__":
    main()

