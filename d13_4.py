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
        self.stack = temp_stack
        return front_element
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        

