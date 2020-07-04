#https://leetcode.com/problems/find-the-duplicate-number/
"""
1)MAke a hash table of the nums
2)Let n be the difference between the length of the hash table and the original array
3)find the differences between the sum of the set and the arr.
4)Divide this difference by the number of repititions to find the number that was repeated
Time Complexity: O(n)
Space Complexity: O(n)
Can also be done by Floyd's Tortoise and Hare
"""
def findDuplicate(nums):
    noRepeat = set(nums)
    n = len(nums) - len(noRepeat)
    repeatedsum = sum(nums)
    setsum = sum(noRepeat)

    return (repeatedsum - setsum)/n

nums = [1,3,4,2,2,6]

print(findDuplicate(nums))