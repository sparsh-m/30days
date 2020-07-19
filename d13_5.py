#https://leetcode.com/problems/valid-parentheses/
#Time Complexity: O(n)
def isValid(s: str):
    stack = list()
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack)>1 and isPair(stack):
            stack.pop()
            stack.pop()
    #if stack is empty in the all pairs have been accounted for
    return not stack

#Checks if the top two elements in the stack match
def isPair(stack):
    return (stack[-2]=="(" and stack[-1]==")") or (stack[-2]=="[" and stack[-1]=="]") or (stack[-2]=="{" and stack[-1]=="}")