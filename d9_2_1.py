#https://leetcode.com/problems/valid-sudoku/submissions/
def isrow(board):
    for i in board:
        if not unit(i):
            return False
    return True
def iscol(board):
    for col in zip(*board):
        if not unit(col):
            return False
    return True
def isbox(board):
    for i in [0,3,6]:
        for j in [0,3,6]:
            square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if not unit(square):
                return False
    return True

def unit(iterable):
    a = [i for i in iterable if i!="."]
    if len(a)!=len(set(a)):
        return False
    return True

def isValidSudoku( board):
    return isrow(board) and iscol(board) and isbox(board)
    
board = [
    ["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board))