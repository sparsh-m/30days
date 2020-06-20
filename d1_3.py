#https://www.interviewbit.com/problems/repeat-and-missing-number-array/
def repeatedNumber(self, A):
    n = len(A)
    a = sum(A) - sum(set(A))
    abDiff = sum(A) - int((n*(n+1)/2))
    b = a - abDiff
    return [a,b]