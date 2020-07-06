#https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
"""
1)Add eacj element to the curr_sum.
2)If curr_sum not in dict add it it to the dict with,
the index of i
3)If curr_sum == 0 means the length of the array traversed till now
is the largest subarry so max_len = i+1
4)If curr_sum == 0 means the length of subarray from the last time curr_sum
was the same till now is the same.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def solve(nums):
    dict={}
    curr_sum=0
    max_len=0
    for i in range(len(nums)):
        curr_sum+=nums[i]

        if curr_sum==0:
            max_len=i+1
        
        if curr_sum in dict:
            max_len=max(max_len,i-dict[curr_sum])
        else:
            dict[curr_sum]=i
    
    return max_len

a = [15, -2, 2, -8, 1, 7, 10, 23]
print(solve(a))