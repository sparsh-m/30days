#https://leetcode.com/problems/set-matrix-zeroes/
def solve(matrix):
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in row:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    
    for j in col:
        for i in range(len(matrix)):
            matrix[i][j] = 0
    
    return matrix

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

solve(matrix)
for i in matrix:
    print(i)