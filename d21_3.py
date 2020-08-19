#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/
#TC:O(N)
#SC:O(N)
def dfs(self,root,s,k):
    if not root:
        return False
    if k-root.val in s:
        return True
    s.add(root.val)
    return self.dfs(root.left, s, k) or self.dfs(root.right, s, k)
    
def findTarget(self, root: TreeNode, k: int) -> bool:
    s = set()
    return self.dfs(root,s,k)

    