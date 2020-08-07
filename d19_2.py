#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def makeTree(prestart, instart, inend, inorder, preorder,d):
            if instart>inend:
                return None
            node = TreeNode(preorder[prestart])
            rootindex = d[preorder[prestart]]

            node.left = makeTree(prestart+1, instart, rootindex-1, inorder, preorder,d)
            node.right = makeTree(prestart + rootindex - instart + 1, rootindex+1, inend, inorder, preorder,d)
            return node
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i 
        return makeTree(0,0,len(inorder)-1, inorder, preorder,d)


i = [4,2,5,1,6,3]
p = [1,2,4,5,3,6]
