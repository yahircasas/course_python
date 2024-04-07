"""
It is commonly said that one human year is equivalent to 7 dog years.
However, this simple conversion fails to recognize that dogs reach adulthood in approximately two years.
As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years,
and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years described in the previous explanation.
Ensure that your program works correctly for conversions of less than two human years and for conversions of two or
more human years. Your program should display an appropriate error message if the user enters a negative number.
"""
# Function to convert human years to dog years
def human_to_dog_years(human_years):
    # Check if input is non-negative
    if human_years < 0:
        return "Error: Please enter a non-negative number."

    # Conversion logic
    if human_years <= 2:
        dog_years = human_years * 10.5  # Conversion for the first two years
    else:
        dog_years = 21 + (human_years - 2) * 4  # Conversion for additional years

    # Return the calculated dog years
    return dog_years

# Test the function with different inputs
human_years = float(input("Enter the number of human years: "))
print("Equivalent dog years:", human_to_dog_years(human_years))

