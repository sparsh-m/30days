#https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/
"""
Time Complexity: O(2*n) => O(N)
Space Complexity: O(N)
"""
def solve(A):
    stack = list()
    max_area = 0
    for i in range(0,len(A)+1):
        while stack and (i==len(A) or A[i] < A[stack[-1]]):
            height = A[stack[-1]]
            stack.pop()
            if stack:
                #assumes that all elements between
                #index i and stack top are greater than
                #height
                area = height*(i-stack[-1]-1)
            else:
                #In case the stack is empty that means
                #the element is the smallest element till now
                area = height*i
            max_area = max(max_area, area)
        #Append the index of the element
        stack.append(i)
    return max_area

print(solve([2,1,5,6,2,3]))