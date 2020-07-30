#https://leetcode.com/problems/longest-common-prefix/submissions/
"""
Time Complexity: O(N*min_len)
Space Complexity: O(1)
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
    min_len = 1000000
    if not strs:
        return ""
    #Finding the length of the shortest string
    for i in strs:
        min_len = min(min_len, len(i))
    res=""
    #Compare the ith element for all min lengths
    for i in range(min_len):
        #Makes sure the ith elements are equal
        equal_flag = 1
        for j in range(1,len(strs)):
            if strs[j][i] != strs[j-1][i]:
                equal_flag = 0
        if not equal_flag:
            return res
        print(strs[0][i])
        res+=strs[0][i]
    return res