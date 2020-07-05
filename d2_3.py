#https://leetcode.com/problems/next-permutation/solution/
"""
1)Start from the rear of the list till index 1.
2)If arr[i]>arr[i-1] start a new loop from the last index till i(let iterator be j)
3)If arr[j]>arr[i-1] swap them and reverse the list from i till the end.
4)If there is no instance of arr[i]>arr[i-1], reverse the whole array
Time Complexity:O(n) In worst case only 2 scans are needed
Space Complexity: O(1), in place operation
"""   
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums)-1
    while i>0:
        if nums[i] > nums[i-1]:
            j = len(nums)-1
            while j>=i:
                if nums[j]>nums[i-1]:
                    nums [j], nums[i-1] = nums[i-1], nums[j]
                    #reversing
                    a=i
                    b=len(nums)-1
                    while(a<b):
                        nums[a], nums[b] = nums[b], nums[a]
                        a+=1
                        b-=1
                    return
                j -= 1
        i -= 1
    
    a=0
    b=len(nums)-1
    while(a<b):
        nums[a], nums[b] = nums[b], nums[a]
        a+=1
        b-=1
    return

nums=[1,2,5,1,7,2]
nextPermutation(nums)
print(nums)