#https://leetcode.com/problems/longest-consecutive-sequence/submissions/
"""
Q)Given an unsorted array of integers, find the length of the longest 
consecutive elements sequence.
1)Iterate over the array
2)If the for every element i if i-1 is not in the set, make curr = 1,
and curr_streak = 1
3)If curr+1 is in set increment curr_streak
4)Update longest streak
Time Complexity: O(n)Amortised
Space Complexity: O(n)
"""
def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak=0
    for i in nums:
        if i-1 not in num_set:
            curr=i
            curr_streak=1
            while curr+1 in num_set:
                curr+=1
                curr_streak+=1

            longest_streak=max(longest_streak, curr_streak)
    return longest_streak
nums = [4,5,6,345,7,5,8,12,9]
print(longestConsecutive(nums))