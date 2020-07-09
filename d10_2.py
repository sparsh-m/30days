#https://leetcode.com/problems/combination-sum-ii/
def combinationSum2(candidates, target):
    res = []
    visited = set()
    helper(res,candidates,visited,target,0,[])
    return res
def helper(res,candidates,visited,target,total,subset):
    if total>=target:
        if total==target:
            k=sorted(subset)
            if k not in res:
                res.append(k)
    else:
        for i in range(len(candidates)):
            if i not in visited:
                visited.add(i)
                helper(res,candidates,visited,target,total+candidates[i],subset+[candidates[i]])
                visited.remove(i)

candidates = [10,1,2,7,6,1,5]
target = 8

ans = combinationSum2(candidates, target)
print(ans)