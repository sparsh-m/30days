#https://leetcode.com/problems/subsets/
"""
Given a set of distinct integers, nums,
return all possible subsets (the power set).
"""
#This method is okay but gives TLE, due to sorting and
# traversing some options twice
"""def subsets(nums):
	visited = set()
	res = []
	def backtracking(subset):
		f = sorted(subset)
		if f not in res:
			res.append(f)
		for i in range(len(nums)):
			if i not in visited:
				visited.add(i)
				#print(subset)
				backtracking(subset+[nums[i]])
				visited.remove(i)
	backtracking([])
	return res
"""
#This is the ideal solution where the required
#subset is only generated once
#			[]
# 		  /  | \
#		1	 2	3
#	   /     |	   \
#	12 		23		31
#   /
#123

#Time Complexity: O(n*2^n)
def subsets(nums):
	def backtracking(start=0, subset=[]):
		if k==len(subset):
			res.append(subset)
		#start prevent repitition
		for i in range(start,len(nums)):
			#backtrack
			backtracking(i+1, subset+[nums[i]])
	res = [[]]
	#For all the powerset of a certain length
	for k in range(1,len(nums)+1):
		backtracking()
	return res


nums = [1,2,3]
l = subsets(nums)
print(l)