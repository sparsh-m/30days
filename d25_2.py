#https://leetcode.com/problems/longest-increasing-subsequence/submissions/
"""

swipe through the array, maintain a subsequence array s of INCREASING numbers
for each new element x
if x larger than s[s.size()-1], append x to s
else find an element that's just larger than x (whose previous is smaller than x)
replace that element with x (above can be done with binary search)(This gives O(logN))
Why is this correct? s is NOT the increasing subsequence we're looking for
However, the length of s is the correct answer
when we replace s[i] with x
we don't change the length of answer, but we changed the potential best candidate
the idea is to try to make each position's number as small as possible
the actual sequence only changes when we append a number, otherwise it's just a
"virtual change", meaning we don't change the current sequence, but we try to
make each number small so we'll have a larger chance to append more numbers
Time Complexity O(N)
"""
def solve(nums):
    if not nums:
            return 0
    dp = []
    dp.append(nums[0])
    for i in range(1, len(nums)):
        flag = 1
        for j in range(len(dp)):
            if nums[i]<=dp[j]:
                dp[j] = nums[i]
                flag = 0
                break
        #print(dp)
        if flag==1:
            dp.append(nums[i])
    print(dp)
    return len(dp)

nums = [0,8,4,12,2]
a = solve(nums)
print(a)

# def solve(nums):
#     dp = [0]*len(nums)
#     for i in range(1, len(nums)):
#         flag = 1:
#         for j in range(i):
#             if nums