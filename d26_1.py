#https://leetcode.com/problems/minimum-path-sum/
#TC:O(N^2)
def minPathSum(grid):
    n,m = len(grid), len(grid[0])
    dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1,len(dp[0])):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    if len(dp)==1:
        return dp[0][-1]

    for i in range(1,len(dp)):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    if len(dp[0])==1:
        return dp[-1][0]
        
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = min(grid[i][j] + dp[i][j-1], grid[i][j] + dp[i-1][j])

    return dp[-1][-1]

grid = [
  [1,3,1]
]

print(minPathSum(grid))