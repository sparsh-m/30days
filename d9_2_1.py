#https://leetcode.com/problems/valid-sudoku/submissions/
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
 according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
#Checks all rows for invalid values
def isrow(board):
    for i in board:
        if not unit(i):
            return False
    return True
#Checks all columns for invalid values
def iscol(board):
    for col in zip(*board):
        if not unit(col):
            return False
    return True
#Checks all boxes for invalid values
def isbox(board):
    for i in [0,3,6]:
        for j in [0,3,6]:
            #to make a square into an array
            square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if not unit(square):
                return False
    return True
#Checks for duplicate element in an iterable
#uses hashing
def unit(iterable):
    a = [i for i in iterable if i!="."]
    return len(a)==len(set(a))

#Calling Function
def isValidSudoku( board):
    return isrow(board) and iscol(board) and isbox(board)

board2 = [
    [".","2","3","4","5","6","7","8","9"],
    ["1",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
    
board = [
    ["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board2))