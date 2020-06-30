#https://leetcode.com/problems/sudoku-solver
#O(n ^ m) where n is the number of possibilities for each square 
#(i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.
def isSafe(board, row, col, num):
	for k in range(9):
		if board[row][k]==num:
			return False
		if board[k][col]==num:
			return False
		if board[3*(row//3)+(k//3)][3*(col//3)+(k%3)]==num:
			return False
	return True

def solve(board):
	print(board)
	for i in range(9):
		for j in range(9):
			if board[i][j] == ".":
				a = "123456789"
				for x in a:
					if isSafe(board, i, j, x):
						board[i][j]=x
						if solve(board):
							return True
						else:
							board[i][j]='.'
				return False
	return True

def solve2(board,row,col):
	if row==9:
		return True
	if col==9:
		return solve2(board,row+1,0)
	if board[row][col]!='.':
		return solve2(board, row, col+1)
	
	for x in "123456789":
		if isSafe(board,row,col,x):
			board[row][col]=x
			print(board[row][col],row,col)
			if solve2(board,row,col+1):	
				return True
			board[row][col]='.'
	return False
board=[
	["5","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."],
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]
	]
#print(helper(board, 0, 0))
print(solve2(board,0,0))

#print(isSafe(board, 2,3,"2"))
