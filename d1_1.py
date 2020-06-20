#https://leetcode.com/problems/find-the-duplicate-number/
def findDuplicate_1(nums):
    n = len(nums)
    rtotal = (n*(n+1))/2
    total = sum(nums)
    
    rsq = (n*(n+1)*((2*n)+1))/6
    sq = 0
    for i in range(n):
        sq += nums[i]**2
    
    aminusb = rtotal - total
    aplusb = (rsq - sq)/aminusb
    
    a = (aplusb + aminusb)/2
    b = aplusb - a
    
    return int(b)

#correct approach
def findDuplicate(nums):
    noRepeat = set(nums)
    n = len(nums) - len(noRepeat)
    repeatedsum = sum(nums)
    setsum = sum(noRepeat)

    return (repeatedsum - setsum)/n

nums = [1,3,4,2,2,6]

print(findDuplicate(nums))