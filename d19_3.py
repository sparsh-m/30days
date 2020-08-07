#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(inorder, ins, ine, postorder, ps, pe, d):
        if ps>pe or ins>ine:
            return None
        node = TreeNode(postorder[pe])
        ri = d[postorder[pe]]
        
        node.left = helper(inorder,ins, ri-1, postorder, ps, ps + ri-ins-1,d)
        node.right = helper(inorder, ri+1, ine, postorder,ps+ri-ins,pe-1,d)
        return node
    d={}
    for i in range(len(inorder)):
        d[inorder[i]] = i
    return helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1,d)