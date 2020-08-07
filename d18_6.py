#recursive
#checks from top to bottom
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

#iterative
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return True
        
        deq = deque()
        deq.append((p,q))
        while deq:
            p,q = deq.popleft()
            if not check(p,q):
                return False
            #if q can too be written as code would have returned false
            #if one of them was None
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True