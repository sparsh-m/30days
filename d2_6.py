#https://leetcode.com/problems/rotate-image/
"""
1)Assume the matrix is made of squares inside squares
2)Starting from the outerrmost square rotate each element one by one
eg
1 2 3               1 2 3
4 5 6   is made of  4   6   and 5
7 8 9               7 8 9

rotate each element in a side one by one
1 goes in place of 3
3 -> 9
9 -> 7
7 -> 1
Time complexity for n*n matrix is O(n^2/8)
"""
def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    #i gives a measure of how into the the matrix you are
    for i in range(rows//2):
        #j is the measure which elements will be shifted
        for j in range(i,cols-1-i):
            k=0
            hold = matrix[i][j]
            #because 4 corners
            while k<4:
                k+=1
                #for i
                a = j
                #for j
                b = cols-1-i

                transfer = matrix[a][b]
                matrix[a][b] = hold
                hold = transfer

                i=a
                j=b
        
    for i in matrix:
        print(i)




matrix =[
  [1,2,3,4,5,6],
  [4,5,6,3,5,7],
  [7,8,9,4,5,7],
  [2,7,3,6,4,2],
  [9,65,4,2,3,2],
  [4,4,5,6,7,3]
]

rotate(matrix)

    