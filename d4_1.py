
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
    maps={}
    for i in range(len(nums)):
        maps[nums[i]] = i

    for i in range(len(nums)):
        if target-nums[i] in maps.keys() and i != maps[target-nums[i]]:
            return [i,maps[target-nums[i]]]

#one pass is better
nums = [3,3,4,2]
print(twoSum(nums, 6))
