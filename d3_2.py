#https://leetcode.com/problems/powx-n/submissions/
def power(x,n):
    ans = 1
    y = abs(n)
    while y>0:
        if y&1 == 1:
            ans *= x
        
        y = y >> 1
        x *= x
    return ans if n>0 else 1/ans
print(power(2,10))