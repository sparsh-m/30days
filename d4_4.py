#https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/
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

a = [1,2,3,4,4,0]
print(solve(a))