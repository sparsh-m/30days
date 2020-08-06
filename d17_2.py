#https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
#recursive
def helper(root, res):
    if root:
        res.append(root.val)
    if root.left:
        helper(root.left, res)
    if root.right:
        helper(root.right, res)
    return res
def sol(root):
    if not root:
        return root
    res = []
    helper(root, res)
    return res
#iterative
def preorderTraversal(self, root: TreeNode) -> List[int]:
    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        if curr:
            stack.append(curr.right)
            res.append(curr.val)
            stack.append(curr.left)
    return res