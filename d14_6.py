#https://leetcode.com/problems/rotting-oranges/submissions/
"""
Time Complexity: O(row*column)

    Add all fresh oranges to fresh_set and append all rotten oranges to rotten_queue.
    
    Use BFS to find all fresh oranges that adjacent to the current rotten orange,
    turn these fresh oranges to rotten and remove these from fresh_set. In the meantime,
    track the steps of turning.
    
    After we finish the turning, if there is still a fresh orange in fresh_set,
    return -1 otherwist return the step.

This is like the chain reaction game
"""
from collections import deque
def orangesRotting(grid):
    row = len(grid)
    col = len(grid[0])
    fresh = set()
    rotten = deque()
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    step = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j]==2:
                rotten.append([i,j,step])
            if grid[i][j]==1:
                fresh.add((i,j))
    while rotten:
        x,y,step = rotten.popleft()
        for dx, dy in dirs:
            if 0<=dx+x<row and 0<=dy+y<col and grid[dx+x][dy+y] == 1:
                grid[dx+x][dy+y] = 2
                #step+1 to count the number of collisions
                rotten.append([dx+x, dy+y, step+1])
                fresh.remove((dx+x, dy+y))
    return -1 if fresh else step

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))