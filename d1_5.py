#https://leetcode.com/problems/maximum-subarray/
"""
Uses KADANE'S ALGORITHM
1)currsum gives the sum from the last non negative to the current till the
it's value remains positive.
2)Iterate over the array and add to currsum is currsum exceeds best sum update
best sum
3)if currsum goes below zero the contiguous subarray is broken therefore reset it to zero
4)the final vaue of bestsum is the answer
"""
def maxSubArray(nums):
    currSum = 0
    bestSum = float('-inf')
    for x in nums:
        #print("Value of x is", x, "\n")
        currSum+=x
        bestSum = max(bestSum, currSum)
        currSum = max(currSum, 0)
    return bestSum