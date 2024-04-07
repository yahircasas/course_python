"""
Positions on a chess board are identified by a letter and a number.
The letter identifies the column, while the number identifies the row,as shown here:
https://cdn2.vectorstock.com/i/1000x1000/53/21/a-chessboard-white-and-bla-vector-22415321.jpg
Write a program that reads a position from the user.
So, for example if the user enters 'a1' then your program should report that the square is black.
if the user enters 'd5' then your program should report that the square is white
"""
# Prompt the user to enter the position on the chessboard
position = input("Enter the position on the chessboard (e.g., 'a1', 'd5'): ")

# Extract the column and row from the input position
column = position[0]  # Extract the first character which represents the column
row = int(position[1])  # Extract the second character which represents the row and convert it to an integer

# Check if the column and row correspond to a black or white square
if (column in 'aceg' and row % 2 == 1) or (column in 'bdfh' and row % 2 == 0):
    print("The square is black.")  # If the conditions are met, the square is black
else:
    print("The square is white.")  # If the conditions are not met, the square is white

