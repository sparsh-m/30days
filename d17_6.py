#Bottom View
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
from collections import deque
def bottomView(root):
    queue = deque()
    d = dict()
    stop = TreeNode(-1)
    
    if root:
        queue.append((root, 0))
        queue.append((stop, -100))
    
    while len(queue)>1:
        temp, level = queue.popleft()
        while temp != stop:
            d[level] = temp.val
            if temp.left:
                queue.append((temp.left, level-1))
            if temp.right:
                queue.append((temp.right, level+1))
            temp, level = queue.popleft()
        queue.append((stop, -100))
    q = d.items()
    q = sorted(q, key = lambda q:q[0])
    print([i[1] for i in q])

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(7)
g = TreeNode(6)

a.left = b
a.right = c
b.right = f
c.left = d
c.right = e
d.left = g

bottomView(a)

