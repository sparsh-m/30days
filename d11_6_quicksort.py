#quicksort
#https://www.geeksforgeeks.org/quick-sort/
#Time Complexity: O(n^2)
#Average Case: O(nlog(n))
"""
Although the worst case time complexity of QuickSort is O(n2) which is more 
than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is
faster in practice, because its inner loop can be efficiently implemented on
most architectures, and in most real-world data. QuickSort can be implemented
in different ways by changing the choice of pivot, so that the worst case rarely
occurs for a given type of data. However, merge sort is generally considered better
when data is huge and stored in external storage. 
"""
def partition(arr, low, high):
    pivot = arr[high]
    j=low
    i=low-1
    for j in range(low, high):
        if pivot>arr[j]:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)

        quicksort(arr, low, p-1)
        quicksort(arr, p, high)

arr = [1,8,3,9,4,5,7] 
quicksort(arr, 0, len(arr)-1)
print(arr)