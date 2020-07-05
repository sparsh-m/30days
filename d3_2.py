#https://leetcode.com/problems/powx-n/submissions/
"""
x & y
    Does a "bitwise and". Each bit of the output is 1 if the 
    corresponding bit of x AND of y is 1, otherwise it's 0. 
x >> y
    Returns x with the bits shifted to the right by y places.
    This is the same as //'ing x by 2**y.
"""
def power(x,n):
    ans = 1
    y = abs(n)
    while y>0:
        if y&1 == 1:
            ans *= x
        
        y = y >> 1
        x *= x
        print(x,ans)
    return ans if n>0 else 1/ans
print(power(2,10))