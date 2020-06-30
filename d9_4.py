#rat in a maze
board = [
	[1,0,0,0],
	[1,1,0,1],
	[0,1,0,0],
	[1,1,1,1]
	]
def isSafe2(board, i, j, N):
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
	helper(board, N, 0, 0, answer)
	return answer

def helper(maze,N, row, col, answer): 
    if row == N - 1 and col == N - 1 and maze[row][col]== 1: 
        answer[row][col] = 1
        return True
       
    if isSafe2(maze, row, col,N) == True: 
        answer[row][col] = 1
        if helper(maze,N, row+1, col, answer) == True: 
            return True
        if helper(board, N,row, col+1, answer) == True: 
            return True
        answer[row][col] = 0
        return False
print(isSafe(board, 0, 1, 4))
answer=solve(board)
for i in answer:
	print(i)
