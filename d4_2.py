#https://leetcode.com/problems/3sum/
def threeSum(nums):
    res = []
    nums.sort()
    length = len(nums)
    for i in range(length-2):
        if nums[i]>0: break
        if i>0 and nums[i]==nums[i-1]: continue
        l, r = i+1, length-1
        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total<0:
                l+=1
            elif total>0:
                r-=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
    return res
#4sum two pointers as it uses less memory
"""
1)If the length of the nums is less than 4 then 4sum isn't possible
so return empty array.
2)sort the array
3)Declare a solution set
4)In n^2 elements explore every pair of elements
5)Now declare two pointers, l and r if nums[l]+nums[r] == target-nums[i]-nums[j]
add the numbers to sol.
6)If nums[l]+nums[r] < target-nums[i]-nums[j], increment l
7)If nums[l]+nums[r] > target-nums[i]-nums[j], decrement r

Time Complexity: O(n^3)
Space Complexity: O(1)
"""
def fourSum_twoPointer(nums, target):
    n = len(nums)
    if n<4:
        return []
    nums.sort()
    solution=set()        
    for i in range(n):
        for j in range(i+1,n):
            curr = target-nums[i]-nums[j]
            l=0
            r=n-1
            while l<r:
                while l==i or l==j:
                    l+=1
                while r==i or r==j:
                    r-=1
                
                if l>=r:
                    break

                if nums[l]+nums[r] == curr:
                    temp = [nums[i],nums[j],nums[l],nums[r]]
                    #print(temp)
                    temp.sort()
                    solution.add(tuple(temp))
                    l+=1
                elif nums[l]+nums[r] > curr:
                    r-=1
                elif nums[l]+nums[r] < curr:
                    l+=1

    s=[]
    for i in solution:
        s.append(list(i))

    return s

nums=[-3,-2,-1,0,0,1,2,3]
target=0
#print(fourSum_twoPointer(nums,target))
