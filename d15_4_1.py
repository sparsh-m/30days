#https://leetcode.com/problems/implement-strstr/submissions/
"""
Gives the index of the needle in the haystack in O(N) time
"""
def strStr(self, haystack: str, needle: str) -> int:
    #If needle is an empty string return 0
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1