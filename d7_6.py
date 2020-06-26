#https://leetcode.com/problems/max-consecutive-ones/submissions/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen=0
        i=-1
        j=0
        while j<len(nums):
            if nums[j]==0:
                maxlen = max(maxlen,j-i-1)
                i=j
            j+=1
        maxlen = max(maxlen,j-i-1)
        return maxlen
