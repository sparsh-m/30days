#https://leetcode.com/problems/shortest-palindrome/
#Naive Solution
#Check if s is palindrome if its not
# remove the last element and chack again
# till the palindrome is found.
# The reverse the list of deleted elements and add it
# to the front of s for the answer
# Time Complexity:O(n^2)#
def isPalindrome(s):
        i,j=0,len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
def shortestPalindrome(s):
    for i in range(len(s),-1,-1):
        if isPalindrome(s[:i]):
            temp = s[i:]
            return temp[::-1]+s
s = "abc"
print(shortestPalindrome(s))
"""
Using Temporary array function of KMP
"""
def solution(text):
    s = text + '$' + text[::-1]
    arr = [0]*len(s)
    i,j = 1,0
    while i<len(s):
        if s[i]==s[j]:
            arr[i] = j+1
            i+=1
            j+=1
        else:
            if j!=0:
                j = arr[j-1]
            else:
                arr[i] = 0
                i+=1
    #gives the inxes from where the
    #palindrome ends
    #eg asdfdsa|rt
    #index of r is the cut point
    cutpoint = arr[-1]
    temp =  text[cutpoint:]
    return temp[::-1] + text