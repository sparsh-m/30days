#find median of an unsorted array.
#https://www.youtube.com/watch?v=RItfXpx3SD4
nums = [1,2,3,4,5,6,7,8]
k = (len(nums)//4)*2

def getmedian(nums, k):
    s=[]
    l=[]
    pivot = nums[0]

    for i in range(1, len(nums)):
        if nums[i]<pivot:
            s.append(nums[i])

    for i in range(1, len(nums)):
        if nums[i]>pivot:
            l.append(nums[i])
    print(pivot,s,l,k)
    if len(s)==k:
        return pivot
    
    if len(s)>k:
        #because the position k stays the same
        return getmedian(s, k)
    
    if len(s)<k:
        #-1 because pivot is removed too
        return getmedian(l,k-len(s)-1)

print(getmedian(nums, k))