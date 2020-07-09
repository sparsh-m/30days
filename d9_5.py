#https://leetcode.com/problems/permutations/
"""
Given a collection of distinct integers, return all possible permutations.
Time Complexity: O(n!)
Space Complexity: O(n!)
"""
def permute(nums):
	#List of all permutations
	res = []
	#
	visited = set()
	#backtracking function
	#subset parameter is the current permutation
	helper(visited, res, [], nums)
	return res

def helper(visited, res, subset, nums):
	#If the length of current permustation is
	#equal to the all no of elements in collection
	#permutation has been completed
	if len(subset)==len(nums):
		res.append(subset)
	#Trying all the elements
	for i in range(len(nums)):
		if i not in visited:
			#Visited holds the numbers that have been included in the permutation
			# it acts a safety function#
			visited.add(i)
			helper(visited, res, subset+[nums[i]], nums)
			print(i,subset)
			visited.remove(i)
nums=["a","b","c","d","e"]
l = permute(nums)
print(l, len(l))

