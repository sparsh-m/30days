def uniquePaths(n,m):
    table = [[1]*m for i in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            table[i][j] = table[i+1][j] + table[i][j+1]
    return table[0][0]
    
print(uniquePaths(4,5))