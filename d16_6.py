#https://leetcode.com/problems/compare-version-numbers/submissions/
"""
Time Complexity:O(N)
Space: O(1)
"""
def compareVersion(self, version1: str, version2: str) -> int:
    v1 = version1.split('.')
    v2 = version2.split('.')
    l1 = len(v1)
    l2 = len(v2)
    v1 = [int(i) for i in v1]
    v2 = [int(i) for i in v2]
    if l1>l2:
        for i in range(l2,l1):
            v2.append(0)
    elif l2>l1:
        for i in range(l1,l2):
            v1.append(0)
    for i in range(len(v1)):
        if v1[i]>v2[i]:
            return 1
        elif v2[i]>v1[i]:
            return -1
    return 0