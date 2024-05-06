"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""


# def compute_average(values):
#     total = sum(values)
#     count = len(values)
#     if count == 0:
#         return 0
#     else:
#         return total / count
#
# def main():
#     values = []
#
#     print("Enter the values enter 0 to finish ->")
#
#     while True:
#         value = float(input("Enter a value: "))
#         if value == 0:
#             if not values:
#                 print("Error: No values provided.")
#                 return
#             else:
#                 break
#         values.append(value)
#
#     average = compute_average(values)
#     print("The average of the values is:", average)
#
# if __name__ == "__main__":
#     main()


cont = 0
my_sum = 0
while True:
    n = float(input('Enter a number: '))
    if n == 0 and cont == 0:
        print('You should enter another value:')
        continue
    elif n == 0:
        break
    else:
        my_sum+=n
        cont+= 1

print(my_sum/cont)

