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