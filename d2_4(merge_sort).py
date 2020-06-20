def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        L=arr[:mid]
        R=arr[mid:]

        L=mergesort(L)
        R=mergesort(R)

        i=0
        j=0
        k=0

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while  j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return arr
arr = [1,3,1,4,3,5,23,5,234,2,1,5,2,4,6,436]
print(mergesort(arr))

