#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    #if one element is the parent of another its the lowest common ancestor
    if root==p or root==q:
        return root
    
    #split into right and left subtree to find the elements
    leftTree = self.lowestCommonAncestor(root.left, p, q)
    rightTree = self.lowestCommonAncestor(root.right, p, q)
    
    #if both left and right subtreee dont have the desired elements
    if leftTree== None and rightTree == None:
        return None
    #if both left and right subtree have passed an element
    #root gives the lowest commont ancestor
    elif leftTree and rightTree:
        return root
    elif leftTree:
        return leftTree
    else:
        return rightTree