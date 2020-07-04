#https://leetcode.com/problems/merge-sorted-array/submissions/
"""
Input format:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

1) Assign pointers longtail and shorttail to the last non zero element of the
given arrays, ie at m-1 and n-1.
2)If the nums1[longtail]>nums2[shorttail] then move the the longtail element
by the length of shorttail+longtail+1, if the opposite is true do the same for
shorttail element.
3)Now complete by filling up with the leftover shorttail elements

"""
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