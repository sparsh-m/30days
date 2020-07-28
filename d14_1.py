#Next smallest element
def solve(nums1,nums2):
    stack = list()
    d = {}
    for i in range(len(nums2)):
        if stack:
            while stack and stack[-1]>nums2[i]:
                d[stack.pop()] = nums2[i]
        stack.append(nums2[i])

    while stack:
        d[stack.pop()] = -1

    for i in range(len(nums1)):
        nums1[i] = d[nums1[i]]
    return nums1

nums2 = [1,3,4,2]
nums1 = [4,1,2]
print(solve(nums1,nums2))