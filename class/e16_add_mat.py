"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).

"""

# def add_matrices(matrix1, matrix2):
#     result = []
#     for row1, row2 in zip(matrix1, matrix2):
#         result_row = [x + y for x, y in zip(row1, row2)]
#         result.append(result_row)
#     return result
#
# def main():
#     # Test cases
#     matrix1 = [[1, -2], [-3, 4]]
#     matrix2 = [[2, -1], [0, -1]]
#     print("Result for matrix1 and matrix2:")
#     print(add_matrices(matrix1, matrix2))
#
#     matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
#     matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
#     print("Result for matrix1 and matrix2:")
#     print(add_matrices(matrix1, matrix2))
#
# if __name__ == "__main__":
#     main()

# Profe
# def add(matrix1, matrix2):
#     result = [[] for _ in range(len(matrix1))]
#     k, j = 0, 0
#     while k < len(matrix1):
#         while j < len(matrix1[k]):
#             result[k].append(matrix1[k][j] + matrix2[k][j])
#             j += 1
#         j = 0
#         k += 1
#     return result
#
# s = add(matrix1=[[1,1,1],[2,3,1],[2,1,3]], matrix2=[[1,1,1],[1,1,1],[1,1,1]])
# print(s)

# Now
def add(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
s = add(matrix1=[[1,1,1],[2,3,1],[2,1,3]], matrix2=[[1,1,1],[1,1,1],[1,1,1]])
print(s)

