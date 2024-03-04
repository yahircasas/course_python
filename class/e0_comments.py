a = 5 # (inline comment) this is an instance of an object
"""
This is a block comment
We can add a lot of lines
"""

def f(x):
    """
    this is a docstring
    A docstring explains what a function does
    :param x:
    :return:
    """
    return x * x  # Returns the square of x

# This comment is outside the if statement

for item in 'python':
    # An indented comment
    if item == 'p':
        # An indented comment
        print('Found!')  # A line comment

# This comment is outside the if statement