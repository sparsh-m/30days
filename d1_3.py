#https://www.interviewbit.com/problems/repeat-and-missing-number-array/
"""
One number is repeated and one number is absent.
1)sum(A) - sum of set(A) gives a, ie the number which was repeated
2)sum(A) = x + a
3)(n*(n+1)/2) = x + b
4)a - b = sum(A) - (n*(n+1)/2)
5)b = a - (a - b)
Time Complexity: O(n)
Space Complexity: O(n)
"""
def repeatedNumber(self, A):
    n = len(A)
    a = sum(A) - sum(set(A))
    abDiff = sum(A) - int((n*(n+1)/2))
    b = a - abDiff
    return [a,b]