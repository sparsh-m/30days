#https://leetcode.com/problems/next-permutation/solution/
def reversal(nums, start):
    i=start
    j=len(nums)-1
    while(i<j):
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
        j-=1
    return nums

def nextPermutation(nums):
    i = len(nums)-1
    while i>0:
        if nums[i] > nums[i-1]:
            j = len(nums)-1
            while j>=i:
                if nums[j]>nums[i-1]:
                    nums [j], nums[i-1] = nums[i-1], nums[j]
                    nums = reversal(nums,i)
                    return nums
                j -= 1
        i -= 1
    return nums

nums = [9,5,6,3,2]
print(nextPermutation(nums))
