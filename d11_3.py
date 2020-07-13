#https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
If all elements are written twice num[i]==num[i+1]
for all values of even i.
If there is a single element introduced in between
then num[i]==num[i+1] where i is odd.

If no element has been introduced in between then
num[mid] == num[mid+1] for all even values of mid, and
num[mid] == mun[mid-1] for all odd values of mid.

If the abouve conditions evaluate to true, start = mid+1
else if there is a disruption right = mid

In the last loop start and end point to the sam element wgich is the answer
Time Complexity: O(log(n))
Space Complexity: O(1)
"""
def singleNonDuplicate(nums):
    start, end = 0,len(nums)-1
    while(start<end):
        mid = start + (end - start)//2
        print(start, mid, end)
        if (mid%2 == 0 and nums[mid]==nums[mid+1]) or (mid%2 == 1 and nums[mid]==nums[mid-1]):
            start = mid+1
        else:
            end = mid
    return nums[end]
nums = [1,1,2,2,3,3,4,5,5]
print(singleNonDuplicate(nums))