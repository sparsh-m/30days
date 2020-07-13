#https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
Find the start be index of the smallest element.
If nums[mid]>nums[start] then the break is not between
them otherwise the break is between them

Now check it the target <= arr[n-1], if so
let end = n-1 else end = start and start = 0.
Then do binary search as normal

Time Complexity:O(log(n))
Space Complexity: O(1)
"""
def binsearch(nums,start,end,target):
    while(start <= end):
        mid = start+(end-start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end = mid-1
    return -1

def search(nums, target):
    lo=0
    hi=len(nums)-1
    if not nums:
        return -1
    if nums[lo]<nums[hi]:
        return binsearch(nums, lo,hi,target)
    else:
        while(hi-lo>1):
            mid = lo + (hi-lo)//2
            print(lo,mid,hi)
            if nums[mid]>=nums[lo]:
                lo=mid
            else:
                hi=mid
        print(lo,mid,hi)
        print(nums[hi])

        if target<=nums[len(nums)-1]:
            return binsearch(nums,hi,len(nums)-1,target)
        else:
            return binsearch(nums, 0, hi, target)


print(search([4,5,6,7,0,1,2],3))