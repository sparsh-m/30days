#https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        
    #O(1)
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)        

    O(n)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #creates a new deque
        tmp = deque()
        #puts all but the the top element in another deque
        while len(self.queue)>1:
            tmp.append(self.queue.popleft())
        #takes out the last element
        popped_element = self.queue.popleft()
        #Assigns tmp to self.queue to avoid copying
        self.queue = tmp
        return popped_element

    #O(n)    
    def top(self) -> int:
        """
        Get the top element.
        """
        #similar to pop
        tmp = deque()
        while len(self.queue)>1:
            tmp.append(self.queue.popleft())
        top_element = self.queue.popleft()
        tmp.append(top_element)
        self.queue = tmp
        return top_element
    #O(1)
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """ 
        return not self.queue
    
    def __str__(self):
        string = ""
        for i in self.queue:
            string+=str(i)
            string+=","
        return string[:len(string)-1]

obj = MyStack()
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj)
print(obj.pop())
print(obj)
print(obj.top())
print(obj.empty())