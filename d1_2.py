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
"""
1)Assign mid and low to the beginning and high to the last index
2)If iterate till mid is less than high
3)If arr[mid] is 1 therefore mid should increment if mid was equal to low, we can swap the values of
arr[mid] and arr[low] so that low has the smaller value
3)If arr[mid] is 0 then it must be handles by low, swap arr[low] and arr[mid],
and since the at arr[low] there cant be assigned a smaller value still, so we can increment low.
4)If arr[high] is 2 then a higher value can't be assigned at index high, so we decrement high to bring it to the next place

Time Complexity:O(n)
Space Complexity: O(n)

"""
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
