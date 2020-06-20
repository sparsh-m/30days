#
#one pass solution
"""def twoSum(nums, target):
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in dict.keys():
            return [map[complement],i]
        map[nums[i]]=i
"""
#two pass solution
def twoSum(nums, target):
    map={}
    for i in range(len(nums)):
        map[nums[i]] = i

    for i in range(len(nums)):
        if target-nums[i] in map.keys() and i != map[target-nums[i]]:
            return [i,map[target-nums[i]]]

#one pass is better
nums = [3,3,4,2]
print(twoSum(nums, 6))
