#https://leetcode.com/problems/roman-to-integer/submissions/
"""
Time Complexity: O(n)

Start loop from the last index if the current element is smaller than the
succeeding element subtract it from the finValue else add it to the finvalue
"""
def romanToInt(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    finVal = vals[s[-1]]
    for i in range(len(s)-2,-1,-1):
        if vals[s[i]]>=vals[s[i+1]]:
            finVal+=vals[s[i]]
        else:
            finVal-=vals[s[i]]
    return finVal