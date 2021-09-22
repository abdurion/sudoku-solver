from boards import *

# to print the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Find an empty cell
def find_empty(arr, empty):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                empty[0] = row
                empty[1] = col
                return True
    return False

# Check if the number is used in the row
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False

# Check if the number is used in the same col
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False

# Check if the number is used in the 3x3 box
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False

# calling the functions inside this function
# to make sure it is valid to assign number here
# row - row % 3 or col - col % 3  -> is just to make sure we are
# at the start of the 3x3 box
# using "not" here, is making sure it will return "True", if the "used" is false
def is_valid(arr, row, col, num):
    return (not used_in_row(arr, row, num) and
    not used_in_col(arr, col, num) and
    not used_in_box(arr, row - row % 3, col - col % 3, num))

# The main function to solve the sudoku board
def solve(arr):
    empty = [0,0]
    
    if not find_empty(arr, empty):
        return True
    
    row = empty[0]
    col = empty[1]

    for num in range(1, 10):
        if is_valid(arr, row, col, num):
            arr[row][col] = num

            # if the assign number is right return true
            if solve(arr):
                return True
            
            # else, assign the cell to 0 
            arr[row][col] = 0

    # Backtrack
    return False


if(solve(board_1)):
    print_board(board_1)
else:
    print ("No solution exists")