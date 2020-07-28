#https://leetcode.com/problems/sliding-window-maximum/submissions/
"""
Time Complexity: O(n)
Dry Run URL: https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190626175333/SlidingWindowMaximum.png

    1.Create a deque to store k elements.
    
    2.Run a loop and insert first k elements in the deque.
    While inserting the element if the element at the back of
    the queue is smaller than the current element remove all those
    elements and then insert the element.
    
    3.Now, run a loop from k to end of the array.
    
    4.Print the front element of the array
    
    5.Remove the element from the front of the queue if they are out of the current window.
    
    6.Insert the next element in the deque. While inserting the element if the element at
    the back of the queue is smaller than the current element remove all those elements and
    then insert the element.
    
    7.Print the maximum element of the last window.

"""
import collections
def solve(nums, k):

    local_max = list()
    #hold the indices of the elements
    queue = collections.deque()

    for i in range(k):
        #if the last element is smaller than the upcoming
        #element pop the old element and add the upcoming one
        while queue and nums[queue[-1]]<nums[i]:
            queue.pop()
        queue.append(i)
    
    #element at the front is greatest and hence the local_max
    local_max.append(nums[queue[0]])

    for i in range(k,len(nums)):
        if queue[0] <= i-k:
            queue.popleft()
        while queue and nums[queue[-1]]<nums[i]:
            queue.pop()
        queue.append(i)
        local_max.append(nums[queue[0]])
    
    return local_max
        
nums = [1,-1]
k = 1


print(solve(nums, k))