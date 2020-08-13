"""
If next element in inorder traversal
is smaller than the previous one
that's not BST.
"""
def isValidBST(self, root: TreeNode) -> bool:
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True