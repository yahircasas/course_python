"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
All three sides of an equilateral triangle have the same length.
An isosceles triangle has two sides that are the same length, and a third side that is a different length.
If all sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that
states the triangle’stype.
"""
# Prompt the user to enter the lengths of the sides of the triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check the type of triangle based on the lengths of its sides
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")  # All sides are equal
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is an isosceles triangle.")  # Two sides are equal
else:
    print("The triangle is a scalene triangle.")  # All sides are different
