#https://leetcode.com/problems/next-greater-element-i/
"""
We use a stack to keep a decreasing sub-sequence, whenever we see a number x
greater than stack.peek() we pop all elements less than x and for all the
popped ones, their next greater element is x.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def solve(nums1,nums2):
    stack = list()
    d = {}
    for i in range(len(nums2)):
        if stack:
            while stack and stack[-1]<nums2[i]:
                d[stack.pop()] = nums2[i]
        stack.append(nums2[i])
    
    for i in range(len(nums1)):
        if d[nums1[i]]:
            nums1[i] = d[nums1[i]]
        else:
            nums1[i] = -1
    return nums1

nums2 = [1,3,4,2]
nums1 = [4,1,2]
print(solve(nums1,nums2))