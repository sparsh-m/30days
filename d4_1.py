#https://leetcode.com/problems/two-sum/
#one pass solution
"""
1)Iterate over nums
2)If the component of element is in the dictionary return the
index of the component and the index of the current element
3)Else add the element and it's index to the hash table
Time Complexity: O(n)
Space Complexity: O(n)
"""
def twoSum(nums, target):
    hmap={}
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in hmap.keys():
            return [hmap[complement],i]
        hmap[nums[i]]=i

#two pass solution
"""
def twoSum(nums, target):
    maps={}
    for i in range(len(nums)):
        maps[nums[i]] = i

    for i in range(len(nums)):
        if target-nums[i] in maps.keys() and i != maps[target-nums[i]]:
            return [i,maps[target-nums[i]]]
"""
#one pass is better
nums = [3,3,4,2]
print(twoSum(nums, 7))
