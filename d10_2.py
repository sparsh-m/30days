#https://leetcode.com/problems/combination-sum-ii/
"""
This is the desired solution
Time Complexity: O(k*2^n)
We need O(k) time to copy new linkedlist
when we get one combination
"""
def combinationSum2(candidates, target):
    def helper(start,visited,target,subset):
        if target==0:
            #Sorting to prevent different permutations
            #of the same set
            k=sorted(subset)
            if k not in res:
                res.append(k)
        elif target>0:
            for i in range(start,len(candidates)):
                if i not in visited:
                    #Since an element can't be reused
                    #it is stored in visited
                    visited.add(i)
                    helper(i,visited,target-candidates[i],subset+[candidates[i]])
                    visited.remove(i)
    res = []
    visited = set()
    helper(0,visited,target,[])
    return res



candidates = [2,5,2,1,2]
target = 5

print(combinationSum2(candidates, target))