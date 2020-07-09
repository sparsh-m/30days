#https://leetcode.com/problems/subsets-ii/
"""
Difference with previous is that duplicate elements are allowed.
H0wever for [1,4,4], [1,4] can only be added to the powerset once

Time Complexity: O(n*2^n)
"""
def subsetsWithDup(nums):
    def backtracking(start=0, subset=[]):
        if k==len(subset):
            #so that subsets is not duplicated
            p=sorted(subset)
            if p not in res:
                #if subset length is equal to len req of the powerset
                res.append(p)
                return
        #start prevent repitition
        for i in range(start,len(nums)):
            #backtrack
            backtracking(i+1, subset+[nums[i]])
    res = [[]]
    #For all the powerset of a certain length
    for k in range(1,len(nums)+1):
        backtracking()
    return res