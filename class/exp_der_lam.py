"""
Write a lambda function that calculates the derivative of a given function f(x)f(x) at a particular point.
"""
def numerical_derivative(f, x0, epsilon=1e-6):
    return (f(x0 + epsilon) - f(x0)) / epsilon

# f(x) como lambda function
f = lambda x: x ** 2 + 3 * x + 2
# Calculate the numerical derivative of f(x) at x = 1
x0 = 1
derivative_value = numerical_derivative(f, x0)

print(f"The numerical derivative of f(x) en x = {x0} es aproximadamente: {derivative_value}")
