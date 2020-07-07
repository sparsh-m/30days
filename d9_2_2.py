#https://leetcode.com/problems/sudoku-solver
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Time Complexity:O(n ^ m) where n is the number of possibilities for each square,
				(i.e., 9 in classic Sudoku) and m is the number of spaces that 
				are blank.
"""	
#To check if a value if correct
def isSafe(board, row, col, num):
	for k in range(9):
		#Checks values in row
		if board[row][k]==num:
			return False
		#Checks value in column
		if board[k][col]==num:
			return False
		#checks

		# if board[3*(row//3)+(k//3)][3*(col//3)+(k%3)]==num:
		# 	return False
	#Checks the square
	i = row - row%3
	j = col - col%3
	for k in range(3):
		for l in range(3):
			if board[i+k][j+l] == num:
				return False
	return True

def solve2(board,row,col):
	#Base case when all rows have been traversed
	if row==9:
		return True
	#All cols in a row have been traversed, calls the
	#function again for the next row
	#and sets the column back to zero
	if col==9:
		return solve2(board,row+1,0)
	#Moves to the next col if the option is prefilled
	if board[row][col]!='.':
		return solve2(board, row, col+1)
	
	#Tries all values of x till a solution is found
	for x in "123456789":
		if isSafe(board,row,col,x):
			#Assign x to the empty space
			board[row][col]=x
			
			#Assuming prev assignment to be correct
			#solve the board further
			if solve2(board,row,col+1):	
				return True
			#If the previous assigned x is
			#correct the code will never reach this
			#This is reached when the next step in 
			board[row][col]='.'
	#Returns false after all options have been exhausted
	#ans true hasn't been returned yet
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
print(solve2(board,0,0))
for i in board:
	print(i)

def p (row,col):
	i = row - row%3
	j = col - col%3
	for k in range(3):
		for l in range(3):
			print(i+k,j+l)
p(4,7)