#https://leetcode.com/problems/combination-sum/submissions/
"""
This is the desired solution
Time Complexity: O(k*2^n)
We need O(k) time to copy new linkedlist
when we get one combination
"""

def solve(candidates, target):
	#These start and end pointers prevent the repetioition which
	# happens in the above case and we have to use sets
	def backtrack(target, start, end, subset):
		if target == 0:
			res.append(subset)
		elif target>0:
			for i in range(start, end):
				print(subset)
				backtrack(target-candidates[i], i, end, subset+[candidates[i]])
	res = []
	backtrack(target, 0, len(candidates) ,[])
	return res
a=[7,2,5,1]
n=9
ans = solve(a,n)
print(ans)

def combinationSum(candidates,target):
	candidates.sort()
	res=[]
	helper(candidates,target,res,0,[])
	return res

def helper(candidates,target,res,total,subset):
	if total>=target:
		if total==target:
			print(subset)
			flag = True
			for k in res:
				if k==sorted(subset):
					flag=False
			if flag:
				res.append(sorted(subset))
	else:
		for i in range(len(candidates)):
			helper(candidates,target,res,total+candidates[i],subset+[candidates[i]])