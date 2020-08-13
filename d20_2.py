#https://leetcode.com/problems/search-in-a-binary-search-tree
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if not root:
        return root
    if root.val == val:
        return root
    elif val<root.val:
        return self.searchBST(root.left, val)
    else:
        return self.searchBST(root.right, val)