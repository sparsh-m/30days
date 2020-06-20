#https://leetcode.com/problems/excel-sheet-column-number/
def titleToNumber(s):
    a = s[::-1]
    total = 0
    for i in range(len(a)):
        total += (ord(a[i])-64)*(26**i)
    return total

s = 'ZY'
print(titleToNumber(s))