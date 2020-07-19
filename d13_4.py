#https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp_stack = list()
        while len(self.stack)>1:
            temp_stack.append(self.stack.pop())
        front_element = self.stack.pop()
        #Unlike queues stacks get reversed when pushed
        #into another stack
        self.stack = temp_stack[::-1]
        return front_element
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        temp_stack = list()
        
        while len(self.stack)>1:
            temp_stack.append(self.stack.pop())
        front_element = self.stack.pop()
        #Since we dont want to remove the first element
        #push it back in
        temp_stack.append(front_element)
        
        self.stack = temp_stack[::-1]
        return front_element


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack