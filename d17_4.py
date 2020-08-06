#https://leetcode.com/problems/binary-tree-right-side-view/submissions/
#Recursive
#Preorder traversal with depth
#Has O(N) space complexity
class Solution:
    def solve(self, res, depth, root):
        if root:
            if depth==len(res):
                res.append(root.val)
        if root.right:
            self.solve(res, depth+1, root.right)
        if root.left:
            self.solve(res, depth+1, root.left)
            
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.solve(res, 0, root)
        return res

#iterative solution
#using level order
def rightSideView(self, root: TreeNode) -> List[int]:
    res = []
    queue = deque()
    if root:
        stop = TreeNode(-1)
        queue.append(root)
        queue.append(stop)
    while len(queue)>1:
        temp = queue.popleft()
        res.append(temp.val)
        while temp!=stop:
            if temp.right:
                queue.append(temp.right)
            if temp.left:
                queue.append(temp.left)
            temp = queue.popleft()
        queue.append(stop)
    return res