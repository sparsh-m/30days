#https://leetcode.com/problems/sqrtx/
"""
Time Complexity: O(log(n))
Space Complexity: O(1)
"""
def mySqrt(x):
    if x==0 or x==1:
        return x
    l=1
    r=x//2
    ans=0
    #terminates when l>r
    while l<=r:
        mid = l+(r-l)//2
        if mid*mid <= x:
            l=mid+1
            ans=mid
        else:
            r = mid-1
    return ans

print(mySqrt(239824025958095820958209483))
