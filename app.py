# to print the board
def print_board(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j])
        print('n')

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

