#https://leetcode.com/problems/balanced-binary-tree/submissions/
def isBalanced(self, root: TreeNode) -> bool:
    self.balanced = True
    def depth(root):
        if not root:
            return 0
        L = depth(root.left)
        R = depth(root.right)
        #if L and R subtree depths differ by more than 1
        if L-R>1 or R-L>1:
            self.balanced = False
        return max(L,R)+1
    depth(root)
    return self.balanced
        