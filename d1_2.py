#https://leetcode.com/problems/sort-colors/
def sortColors_1(nums):
    front = 0
    back = len(nums)
    for num in nums:
        if num == 0:
           nums[front] = num
           front += 1
        if num == 2:
            back -= 1

    for i in range(front, back):
        nums[i] = 1

    for i in range(back, len(nums)):
        nums[i] = 2

#correct approach traverses only once
def sortColors(a):
    low = 0
    mid = 0
    high = len(a)-1
    while(mid<=high):
        if a[mid] == 0:
            a[mid], a[low] = a[low], a[mid]
            low += 1
            mid += 1
        elif(a[mid] == 1):
            mid += 1
        else:
            a[high], a[mid] = a[mid], a[high]
            high -= 1

nums = [1,1,1,0]
sortColors(nums)
print(nums)
#print(sort012(nums, len(nums)))
