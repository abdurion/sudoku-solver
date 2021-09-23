import numpy as np
from boards import * 

# check rows, columns, boxes before assigning a number
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    box_row = (row - row % 3)
    box_col = (col - col % 3)

    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        solve(board)

                        board[row][col] = 0

                return
    print(np.matrix(board))
                        
solve(board_1)