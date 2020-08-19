#https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
#TC:O(N^2)
def solve(nums):
    sumStore = [i for i in nums]
    #seqStore = [i for i in range(len(nums))]

    i=1
    while i<len(nums):
        j=0
        while j<i:
            if nums[j]<nums[i]:
                sumStore[i] = max(sumStore[i], sumStore[j]+nums[i])
            j+=1
        i+=1
    print(nums)
    print(sumStore)
    return max(sumStore)

nums = [10, 5, 4, 3]
print(solve(nums))