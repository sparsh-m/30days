#https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
    currSum = 0
    bestSum = float('-inf')
    for x in nums:
        #print("Value of x is", x, "\n")
        currSum+=x
        bestSum = max(bestSum, currSum)
        currSum = max(currSum, 0)
    return bestSum