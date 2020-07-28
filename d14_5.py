#https://leetcode.com/problems/min-stack/discuss/49031/Share-my-Java-solution-with-ONLY-ONE-stack
"""
Space Complexity:O(n)
"""
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = list()
#         self.minStack = list()
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if self.minStack and self.minStack[-1]<x:
#             self.minStack.append(self.minStack[-1])
#         else:
#             self.minStack.append(x)

#     def pop(self) -> None:
#         self.minStack.pop()
#         return self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]

"""
Space Complexity: O(1)
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minNo = -1
    def push(self, x: int) -> None:
        if not self.stack:
            #In case the stack is empty
            self.stack.append(x)
            self.minNo = x
        elif self.minNo > x:
            #If the element to be added is smaller than minNo
            #It replaces the min no
            #also, in the stack a x is modified and entered
            #this is done so that the added element is smaller than
            #the x
            #this helps while poping and topping and the numbers greater
            #than x are returned simply however numbers smaller than minNo
            #indicate that the minNo no has to be updated and the manipulated value
            #of top can be passed back
            self.stack.append(2*x - self.minNo)
            self.minNo = x
        else:
            self.stack.append(x)
    
    def pop(self) -> None:
        if self.stack[-1]<self.minNo:
            self.minNo = self.minNo*2 - self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1]<self.minNo:
            return self.minNo
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minNo

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.top())
obj.pop()
print(obj.top())
obj.pop()
print(obj.top())
