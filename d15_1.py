#https://leetcode.com/problems/reverse-words-in-a-string/
"""
Time Complexity: O(1)
Space Complexity: O(n)

Since python has immutable strings the reversal can't
be truly in place
"""
#using two pointers
def reverseWords(s):
    s = " "+s+" "
    res = ""
    start = end = -1
    for i in range(len(s)-2,0,-1):
        #If suceeded by a space its the end
        if s[i+1] == " " and s[i] != " ":
            end = i
        #If preceeded by a space it's start
        if s[i-1] == " " and  s[i] != " ":
            start = i
            res = res + " " + s[start:end+1]
    return res[1:]

s = "the sky is blue"
print(reverseWords(s)) 