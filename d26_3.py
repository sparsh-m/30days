#To check if a set of numbers can generate a subsequence
def subsetSum(nums, sum):
    dp = [[1 for i in range(sum+1)]for i in range(len(nums))]
    for i in range(1,len(dp[0])):
        if i-nums[0]==0:
            dp[0][i]  = 1
        else:
            dp[0][i] = 0
    
    for i in range(1, len(nums)):
        for j in range(1,len(dp[0])):
            if j>=nums[i]:
                if dp[i-1][j-nums[i]]==1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] 
            else:
                dp[i][j] = dp[i-1][j]
        
    # for i in dp:
    #     print(i)
    
    return 'Yes' if dp[-1][-1]==1 else 'No'

nums = [2,3,7]
print(subsetSum(nums, 11))
