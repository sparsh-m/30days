#https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        self.helper(res,candidates,visited,target,0,[])
        return res
    def helper(self,res,candidates,visited,target,total,subset):
        if total>=target:
            if total==target:
                k=sorted(subset)
                if k not in res:
                    res.append(k)
        else:
            for i in range(len(candidates)):
                if i not in visited:
                    visited.add(i)
                    self.helper(res,candidates,visited,target,total+candidates[i],subset+[candidates[i]])
                    visited.remove(i)
