#https://leetcode.com/problems/permutations/
def permute(nums):
	res = []
	visited = set()
	helper(visited, res, [], nums)
	return res
def helper(visited, res, subset, nums):
	if len(subset)==len(nums):
		res.append(subset)
	for i in range(len(nums)):
		if i not in visited:
			visited.add(i)
			helper(visited, res, subset+[nums[i]], nums)
			print(i,subset)
			visited.remove(i)
nums=["a","b"]
l = permute(nums)
print(l)

"""def permute(self,nums):
	res = []
	visted = set()
	self.helper(res,visited,[],nums)
	return res

def helper(self,res,visited,subset,nums):
	if len(subset)==len(nums):
		res.append(subset)
	for i in range(len(nums)):
		if i not in visited:
			visited.add(i)
			self.helper(res,visited,subset+[nums[i]],nums)
			
			visited.remove(i)
	
"""
