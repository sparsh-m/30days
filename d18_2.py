#https://leetcode.com/problems/maximum-depth-of-binary-tree
#iterative
#dfs
def maxDepth(self, root: TreeNode) -> int:
    res = 0
    stack = []
    if root:
        stack.append((root, 1))
    
    while stack:
        curr, level = stack.pop()
        res = max(res, level)
        if curr.left:
            stack.append((curr.left, level+1))
        if curr.right:
            stack.append((curr.right, level+1))
    return res

#recursive
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))