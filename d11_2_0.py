#https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/
"""
Bruteforce: Merge into a single array, and then find media
Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""
def matrixMedian(matrix):
    arr = matrix[0]

    for i in range(1,len(matrix)):
        arr = merge(arr, matrix[i])
        print(arr)
    mid = len(arr)//2
    return arr[mid]

def merge(a,b):
    arr=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            arr.append(a[i])
            i+=1
        else:
            arr.append(b[j])
            j+=1
    while i>len(a):
        arr.append(a[i])
        i+=1
    while j<len(b):
        arr.append(b[j])
        j+=1
    return arr

arr = [
    [1,3,5],
    [2,6,9],
    [3,6,9]
]

print(matrixMedian(arr))