#https://leetcode.com/problems/xor-queries-of-a-subarray/
"""
XOR: Return 1 id bits are different, 0 if same.
XOR property
a^b^c = x
b^c = x^a
Time Complexity:O(n) 
"""
def xor(arr, queries):
    n = len(arr)
    for i in range(1,n):
        arr[i]=arr[i]^arr[i-1]
    
    solution=[]
    for x in range(len(queries)):
        i=queries[x][0]
        j=queries[x][1]
        if i==0:
            solution.append(arr[j])
        else:
            temp = arr[i-1] ^ arr[j]
            solution.append(temp)
    
    return solution

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]

print(xor(arr,queries))