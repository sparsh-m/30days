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

    while i<=left and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            i+=1
            k+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=mid-i+1
            j+=1
            k+=1

    while i<=left:
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

arr = [8,4,2,1]
print("The number of inversions", mergesort(arr))
