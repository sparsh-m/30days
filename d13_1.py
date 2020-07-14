#implementing a stack
#using deque as it doesnt allocate contiguous memory like list
#lifo
myStack = []
myStack.append('a')
myStack.append('c')
myStack.append('e')
myStack.append('g')

while myStack:
    print(myStack.pop())

#implementing a deque
#fifo
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)

while d:
    print(d.popleft())