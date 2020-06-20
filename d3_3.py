#https://leetcode.com/problems/factorial-trailing-zeroes/
from math import floor
def solve(n):
    zeroCnt = 0
    while n > 0:
        n = floor(n/5); zeroCnt += n
    
    return zeroCnt

print(solve(345))