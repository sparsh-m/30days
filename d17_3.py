https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
#Recursive Solution
def helper(root,res):
    if root.left:
        helper(root.left,res)
    if root.right:
        helper(root.right,res)
    if root:
        res.append(root.val)
def postorderTraversal( root: TreeNode) -> List[int]:
    if not root:
        return root
    res = []
    self.helper(root, res)
    return res

#iterative solution
def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            while stack and not curr:
                temp = stack.pop()
                if temp.right and stack:
                    if stack[-1] == temp.right:
                        curr = stack.pop()
                        stack.append(temp)
                        break
                res.append(temp.val)
        return res