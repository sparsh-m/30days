def nqueen(n):
    board = [[0 for j in range(n)] for i in range(n)]
    if solveUtil(board, 0, n):
        for i in board:
            print(i)

def isSafe(board, n, row, col):
    i=0
    while i<=row:
        if board[i][col]:
            return False
        i+=1
    i=row
    j=col
    while i>=0 and j>=0:
        if board[i][j]:
            return False
        i-=1
        j-=1
    i=row
    j=col
    while i>=0 and j<n:
        if board[i][j]:
            return False
        i-=1
        j+=1
    return True

def solveUtil(board, row, n):
    if row>=n:
        return True

    for j in range(n):
        if isSafe(board, n, row, j):
            board[row][j]=1
            if solveUtil(board, row+1, n):
                return True
            board[row][j]=0
    return False

print(nqueen(4))