#https://leetcode.com/problems/excel-sheet-column-number/

"""
same logic as '10001' = 1*2**4 + 0*2**3 + 0*2**2 + 0*2**1 + 1*2**0
"""
def titleToNumber(s):
    a = s[::-1]
    total = 0
    for i in range(len(a)):
        total += (ord(a[i])-64)*(26**i)
    return total

s = 'ZY'
print(titleToNumber(s))