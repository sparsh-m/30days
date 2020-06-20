#https://leetcode.com/problems/merge-sorted-array/submissions/
def solve(nums1, m, nums2, n):
    longtail = m-1
    shorttail = n-1
    while(longtail>=0 and shorttail>=0):
        if nums1[longtail]>nums2[shorttail]:
            nums1[longtail+shorttail+1] = nums1[longtail]
            longtail -= 1
        else:
            nums1[longtail+shorttail+1] = nums2[shorttail]
            shorttail -= 1

    while(shorttail >=0):
        nums1[shorttail] = nums2[shorttail]
        shorttail -= 1

nums1 = [0]
nums2 = [2]
m = 0
n = 1

solve(nums1,m,nums2,n)
print(nums1)