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
			#if subset length is equal to len req of the powerset
			res.append(subset)
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

"""def subsets(nums):
	def backtrack(first = 0, curr = []):
		# if the combination is done
		print(len(curr),k)
		if len(curr) == k:
			output.append(curr)
			return
		for i in range(first, n):
			# add nums[i] into the current combination
			#curr.append(nums[i])
			# use next integers to complete the combination
			backtrack(i + 1, curr+[nums[i]])
			# backtrack
			#curr.pop()
	
	output = []
	n = len(nums)
	for k in range(n + 1):
		backtrack()
	return output
"""
nums = [1,2,3,4,5,6,7,8,9,0]
l = subsets(nums)
print(l)