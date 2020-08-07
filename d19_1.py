#https://leetcode.com/problems/binary-tree-maximum-path-sum/
def maxPathSum(self, root: TreeNode) -> int:
    self.maxpath = -100000
    def help(root):
        if not root:
            return 0
        #0 is there so that the negative values arent added
        L = max(help(root.left),0)
        R = max(help(root.right),0)
        #the maxpath is the sum of root val + max left and right gains
        self.maxpath = max(self.maxpath, L+R+root.val)
        #returns the max of the two branches to it's parents
        return max(L,R)+root.val
    help(root)
    return self.maxpath
    