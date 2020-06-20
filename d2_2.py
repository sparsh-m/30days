#https://leetcode.com/problems/pascals-triangle/
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