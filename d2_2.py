#https://leetcode.com/problems/pascals-triangle/
"""
1)If num_rows == 0 return 0
2)If num_rows is 1 or 2 return hardcoded solution.
3)If num_rows is greater than zero, for ith row, arr[i][0] = 1 or arr[i][i] = 1
4)arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

Time Complexity: O(num_rows^2/2)=O(n^2)
Space Complexity: o(num_rows^2)
"""
def sol(A):
    sol = []
    if(A==0):
        return []
    elif (A == 1):
        sol.append([1])
    elif(A == 2):
        sol = [[1],[1,1]]
    else:
        sol = [[1],[1,1]]
        for i in range(2, A):
            solLine = []
            for j in range(i+1):
                if(j == 0 or j == i):
                    solLine.append(1)
                else:
                    solLine.append(sol[i-1][j-1] + sol[i-1][j])
            sol.append(solLine)
    return sol

print(sol(5))