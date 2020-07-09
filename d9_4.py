#rat in a maze
"""
Time Complexity: O(2^m), 2 as the mouse can go down of right
                m is the number of empty boxes.
Can be done in Space Complexity O(1)
"""
board = [
	[1,0,0,0],
	[1,1,0,1],
	[0,1,0,0],
	[1,1,1,1]
	]
def isSafe2(board, i, j, N):
    #Check if i and j are in bounds and boar[i][j] is valid in itself
	if i>=0 and i<N and j>=0 and j<N and board[i][j]==1:
		return True
	return False
def isSafe( board, i, j, N):
    if i>=0 and i<N and j>= 0 and j<N and board[i][j]==1: 
        return True
    return False

def solve(board):
	N = len(board)
	answer = [[0 for i in range(N)] for i in range(N)]
    #Backtracking function with row and col index as parameter
	helper(board, N, 0, 0, answer)
	return answer

def helper(maze,N, row, col, answer):
    #Base Case
    if row == N - 1 and col == N - 1 and maze[row][col]== 1: 
        answer[row][col] = 1
        return True
    #Safety Function  
    if isSafe2(maze, row, col,N) == True: 
        answer[row][col] = 1
        #Check both right and down blocks
        if helper(maze,N, row+1, col, answer) == True: 
            return True
        if helper(board, N,row, col+1, answer) == True: 
            return True
        #If none are possible return False
        answer[row][col] = 0
        return False
print(isSafe(board, 0, 1, 4))
answer=solve(board)
for i in answer:
	print(i)
