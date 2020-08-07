#https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
    return res

#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    if root:
        stop = TreeNode(-1)
        queue = deque()
        queue.append(root)
        queue.append(stop)
    while len(queue)>1:
        if len(res)%2 == 0:
            level = []
            temp = queue.popleft()
            while temp!=stop:
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                temp = queue.popleft()
            queue.appendleft(stop)
        else:
            level = []
            temp = queue.pop()
            while temp!=stop:
                level.append(temp.val)
                if temp.right:
                    queue.appendleft(temp.right)
                if temp.left:
                    queue.appendleft(temp.left)
                temp = queue.pop()
            queue.append(stop)
        res.append(level)
    return res