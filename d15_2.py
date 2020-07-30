#https://leetcode.com/problems/longest-palindromic-substring/
"""
Brute Force Time Complexity: O(n^3)
My Solution: O(N^2)
"""
def solution(s):
    if not s or len(s)<=1:
        return 0
    start=0
    end=0

    for i in range(len(s)):
        #checks palindrome assuming odd length
        len1 = expandFromMiddle(s, i, i)
        #checks palindrome assuming even length
        len2 = expandFromMiddle(s, i, i+1)
        #take the maximum
        length = max(len1, len2)
        #defines the boundaries of the substring
        #this is adjusted according to the lenght of the
        #palindrome substring
        if length > end-start+1:
            start = int(i-(int((length-1)/2)))# to prevent out of bounds error
            #i is the current indice
            end = int(i+int(length/2))
    return s[start:end+1]

#Checks palindrome and return s the length of the palindrome
#between the given positions
def expandFromMiddle(s, left, right):
    if not s or left>right:
        return 0
    
    while left>=0 and right<len(s) and s[left] == s[right]:
        left-=1
        right+=1
    #Since we are dealing with indices
    print (left, right)
    #because of indices
    return right-left-1

s = "babab"
l=expandFromMiddle(s,2,2)
print(l)