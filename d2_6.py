def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows//2):
        for j in range(i,cols-1-i):
            k=0
            hold = matrix[i][j]
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
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

rotate(matrix)

    