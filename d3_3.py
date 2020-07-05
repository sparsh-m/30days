#https://leetcode.com/problems/factorial-trailing-zeroes/
"""
Number of zeros is equal to the number of 5s.
Since 25 is 5*5, there are also numers 5*1,5*2,5*3,5*4 less than it
so we calculate numer of fives till 25 by 25//5 -> 5, but no of 5s under
25 is 6. 
This happens because 25 is 5*5 therefore two 5s as its factors.
so now n=5
and 5/5->1 which will be added to toal no of fives.

This can be used to find out how many instances of a factor are there in a factorial.
"""
from math import floor
def solve(n):
    zeroCnt = 0

    while n > 0:
        n = floor(n/5); zeroCnt += n
    
    return zeroCnt

print(solve(25))