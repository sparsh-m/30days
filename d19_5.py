#https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#Explanation by bboczeng
#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!
#each node is traversed twice
def flatten(self, root: TreeNode) -> None:
    if not root:
        return 
    node = root
    while node:
        if node.left:
            pre = node.left
            while pre.right:
                pre = pre.right
            pre.right = node.right
            node.right = node.left
            node.left = None
        node = node.right
    