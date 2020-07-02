#https://leetcode.com/problems/partition-equal-subset-sum/
#backtracking isnt good enough for the question
def canPartition(nums):
	visited = set()
	total = sum(nums)
	return backtrack(nums,visited,[],total)
def backtrack(nums,visited,path,total):
	if sum(path) == total-sum(path):
		return True
	for i in range(len(nums)):
		if i not in visited:
			visited.add(i)
			if backtrack(nums,visited,path+[nums[i]],total):
				return True
			visited.remove(i)
	return False
	
nums = [28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16
,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,
92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,
42,26,8,87,99,1,16,79]
print(canPartition(nums))
