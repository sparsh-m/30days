#Top View
from collections import deque
#each elemnent is assumed to be one the number line with root at 0
# root.right at 1 and root.left at -1, and so on and so forth
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):
    d = dict()
    queue = deque()
    if root:
        stop = TreeNode(-1)
        queue.append((root, 0))
        queue.append((stop, -100))
    while len(queue)>1:
        temp, level = queue.popleft()
        while temp!=stop:
            #element for a level is never changed
            if level not in d:
                d[level] = temp.val
            if temp.right:
                queue.append((temp.right, level+1))
            if temp.left:
                queue.append((temp.left, level-1))
            temp, level = queue.popleft()
        queue.append((stop, -100))
    q = {key:d[key] for key in sorted(d.keys())}
    print(list(q.values()))

def levelOrder(root):
    res = []
    if root:
        stop = TreeNode(-1)
        queue = deque()
        queue.append(root)
        queue.append(stop)
    
    while len(queue)>1:
        layer = []
        temp = queue.popleft()
        while temp!=stop:
            layer.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            temp = queue.popleft()
        queue.append(stop)
        res.append(layer)
        #print(res)
    print(res)
    return res

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

topView(a)