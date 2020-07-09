#https://leetcode.com/problems/permutation-sequence/
"""
Backtracking will give tle.
"""
def getPermutation(n,k):
    def backtrack(substring,visited,res):
        if len(substring)==n:
            res.append(substring)
        for i in range(1,n+1):
            #print(i+1)
            if i not in visited:
                visited.add(i)
                backtrack(substring+str(i), visited,res)
                visited.remove(i)
    visited=set()
    res=[]
    backtrack("",visited,res)
    return res[k-1]
"""
Time Complexity
"""

def getPermutation( n, k):
        nums = [str(i) for i in range(1, n+1)]
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            #to find the permutation in the kth position
            #(n-1)! strings with with n length and one fixed position
            #id = k/(n-1)! gives the index of the fixed number to be chosen
            #k % (n-1)! positions left
            id = k // fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            #to prevent repition
            nums.pop(id)
        return ''.join(ans)
print(getPermutation(4,14))