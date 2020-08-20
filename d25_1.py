#https://leetcode.com/problems/maximum-product-subarray/
#Time complexity: O(N)
#Space Complexity: O(1)
"""

    1) Current Element is a positive integer:
    -1,6,2  3
    prev max = 12
    prev max * curr= 12*3

    2) Current element is a negative integer:
    -1,6,2 -2
    prev max = 12
    prev min * curr -12 * -2 = 24

    3)Current element is larger
    -1,-1,-1 7
    prev max = 1
    prev min = -1

    new max = 7
    new min = -7
"""
def maxproduct(nums):
    prev_max = nums[0]
    prev_min = nums[0]
    ans = nums[0]
    for i in range(1,len(nums)):
        curr_max = max(nums[i], prev_max*nums[i], prev_min*nums[i])
        curr_min = min(nums[i], prev_max*nums[i], prev_min*nums[i])
        ans = max(ans, curr_max)
        prev_max = curr_max
        prev_min = curr_min
    return ans