#https://leetcode.com/problems/set-matrix-zeroes/
"""
1)For any element arr[i][j] in the mxn matrix that is zero
add i to a row set and add j to a col set.
2)iterate the row set and set the whole rows mentioned as zero
3)iterate the col set and do the same

Time Complexity:O(m*n)
Space Complexity: Not O(1) as the sets require memory.

Better SOlution:
We can rather use the first cell of every row and column as a flag.
This flag would determine whether a row or column has been set to zero. 
This means for every cell instead of going to M+NM+NM+N cells and setting
it to zero we just set the flag in two cells.
Time Complexity: O(m*n)
Space Complexity: O(1)
"""
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