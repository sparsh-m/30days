"""
inversion how many times position changes in an array during merge sort
1)Initiate merge sort left and right trees return an inversion numer
3)This number is further incremented upon merging
eg [8,4,2,1]
                    8,4,2,1
            8,4                 2,1
        8       4           2         1
            4,8(1)              1,2(1)
                    1,2,4,8(2+2)inverions as both 1 and two are placed bofore 8 and 4
Total 6 inversion.
Time Complexity: O(nlog(n))
Space Complexity: O(n), temp arr
"""
def mergesort(arr):
    n = len(arr)
    temp_arr=[0]*n
    return _mergesort(arr, temp_arr, 0, n-1)

def _mergesort(arr, temp_arr, left, right):
    inv_count = 0
    if left<right:
        mid=(left+right)//2
        inv_count += _mergesort(arr, temp_arr, left, mid)
        inv_count += _mergesort(arr, temp_arr, mid+1, right)

        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

def merge(arr, temp_arr, left, mid, right):
    inv_count = 0
    i=left
    k=left
    j=mid+1

    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            i+=1
            k+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=mid-i+1
            j+=1
            k+=1

    while i<=mid:
        temp_arr[k]=arr[i]
        i+=1
        k+=1
    
    while j<=right:
        temp_arr[k]=arr[j]
        j+=1
        k+=1
    
    for i in range(left, right+1):
        arr[i]=temp_arr[i]

    return inv_count

arr = [4,5,6,1,2,3]
print("The number of inversions", mergesort(arr))
