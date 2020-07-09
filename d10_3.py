#https://leetcode.com/problems/palindrome-partitioning
"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Time Complexity: O()
"""
def partition(self, s):
    res=[]
    self.backtrack(s,[],res)
    return res

#Checks Palindrome
def isPal(self,s):
    return s==s[::-1]

def backtrack(self,s,substring,res):
    #When i becomes len(s) s[i:] becomes empty
    #and the loop terminates
    if not s:
        res.append(substring)
        return
    #starts from 1 as i gives the end index of substring
    for i in range(1,len(s)+1):
        if self.isPal(s[:i]):
            #s[i:] gives the left over string
            self.backtrack(s[i:],substring+[s[:i]],res)