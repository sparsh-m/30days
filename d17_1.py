#https://leetcode.com/problems/binary-tree-inorder-traversal
#Recursive
def inOrder(root, res):
    if root.left:
        self.inOrder(root.left, res)
    if root:
        res.append(root.val)
    if root.right:
        self.inOrder(root.right, res)
def inorderTraversal(root):
    if not root:
        return root
    res = []
    inOrder(root, res)
    return res

#Iterative
def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    res = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res