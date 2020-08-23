def perm(nums):
    res = []
    helper([], nums, [], res)
    return res
def helper(visited, nums, subset, res):
	if len(nums) == len(subset):
		res.append(subset)
	else:
		for i in range(len(nums)):
			if i not in visited:
				visited.append(i)
				helper(visited, nums, subset + [nums[i]], res)
				visited.remove(i)

nums=["a","b","c"]
print(perm(nums))
