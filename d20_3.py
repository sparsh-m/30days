#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
#TC:O(N)
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.solve(nums, 0, len(nums))
    
    def solve(self, nums, start, end):
        while start<end:
            mid = (end+start)//2
            root = TreeNode(nums[mid])
            root.left = self.solve(nums, start, mid)
            root.right = self.solve(nums, mid+1, end)
            return root
        return None