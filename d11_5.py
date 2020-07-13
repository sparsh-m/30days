#https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

"""
Similar to median question, this code is for
the Kth largest element.

Doesn't work with duplicate numbers
"""
def search(nums1,nums2,k):
    MAX = 9223372036854775807
    MIN = -9223372036854775808
    #which is the smaller array
    if len(nums1)<=len(nums2):
        short = nums1
        long = nums2
    else:
        short = nums2
        long = nums1
    #Binary Search
    start = len(short)-k
    end = len(short)
    while start<=end:
        part_x = start + (end-start)//2
        part_y = len(long) - (len(short) - start)//2

        #MIN MAX for edge cases 
        #if no element on the left side short as in the case part_x = 0
        # maxleftx becomes MIN 
        maxleftx = MIN if part_x == 0 else short[part_x-1]
        minrightx = MAX if part_x == len(short) else short[part_x]

        maxlefty = MIN if part_y ==0 else long[part_y-1]
        minrighty = MAX if part_y == len(long) else long[part_y]
        
        if maxleftx<=minrighty and maxlefty<=minrightx:
            break
        elif maxleftx > minrighty:
            end-=1
        else:
            start+=1
    return min(minrightx, minrighty)

nums1 = [1,4,8,10]
nums2 = [1,2,4,8,10]

i = search(nums1,nums2,3)
print(i)