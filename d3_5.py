#https://leetcode.com/problems/unique-paths/
"""
1)Since final destination lies in arr[n-1][m-1], now of paths from
any block in row n-1 and col m-1 is 1.
2)For any other block you can either go right, or go down, therefore
the total path from that block is sum of paths from down bloack and right
adjacent block.

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
def uniquePaths(n,m):
    table = [[1]*m for i in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            table[i][j] = table[i+1][j] + table[i][j+1]
    for k in table:
    	print(k)
    return table[0][0]
    
print(uniquePaths(4,5))