#https://leetcode.com/problems/symmetric-tree/submissions/
#recursive
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    def mirror(l,r):
        if not l and not r:
            return True
        if not l:
            return False
        if not r:
            return False
        return l.val==r.val and mirror(l.left, r.right) and mirror(l.right, r.left)
    return mirror(root.left, root.right)

#iterative
d = deque()
        d.append((root, root))
        while d:
            a,b = d.popleft()
            if not a and not b:
                continue
            if not a or not b:
                return False
            elif a.val != b.val:
                return False
            d.append((a.left, b.right))
            d.append((a.right, b.left))
        return True 