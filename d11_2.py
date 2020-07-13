#https://leetcode.com/problems/median-of-two-sorted-arrays
"""
A median should have an equal number of elements,
on both of it's side in an sorted array.

Suppose Two arrays 
x1, x2, x3, x4, x5, x6
y1, y2, y3, y4, y5, y6, y7, y8

Partition them such that left side and right side have an equal no of
elements.

Left Side(7 elemnets)   Right Side(7 elements)
x1, x2,              | x3, x4, x5, x6
y1, y2, y3, y4, y5,  | y6, y7, y8

y5<=y6(given)
x2<=x3(given)

So, if
y5<=x3
x2<=y6
then left side is definately smaller than the right side.

Now max(x2, y5) will be closest to the median from the left side.
and min(x3, y6) will be closest to the median from the right side.

Avg(max(x2, y5), min(x3, y6)) will give the median

If we had an odd number of elements in total, then left side
would have been bigger and max(x2, y5) would have given the median.

During Binary search if maxleftx > minrighty then decrement end by 1
if maxlefty > minrightx increment start by 1

Time Complexity:()
"""

def myMedian(nums1, nums2):
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
    start = 0
    end = len(short)

    while start<=end:
        part_x = (start+end)//2
        #+1 as it works well with both even and odd nos of elements
        part_y = ((len(short)+len(long)+1)//2)-part_x

        #MIN MAX for edge cases 
        #if no element on the left side short as in the case part_x = 0
        # maxleftx becomes MIN 
        maxleftx = MIN if part_x ==0 else short[part_x-1]
        minrightx = MAX if part_x == len(short) else short[part_x]

        maxlefty = MIN if part_y ==0 else long[part_y-1]
        minrighty = MAX if part_y == len(long) else long[part_y]
        
        if maxleftx<=minrighty and maxlefty<=minrightx:
            break
        elif maxleftx > minrighty:
            end-=1
        else:
            start+=1
    
    if (len(short)+len(long)) % 2 == 0:
        return (max(maxleftx,maxlefty) + min(minrightx,minrighty))/2
    else:
        return max(maxleftx,maxlefty)

# nums1 = [1,3,8,9,15]
# nums2 = [7,11,18,19,21,25]
nums1 = [1,2,3,4]
nums2 = [5,6,7,8]
print(myMedian(nums1, nums2))