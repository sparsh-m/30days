#https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
#Smallest element
def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack=[]
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if not k-1:
            return curr.val
        else:
            k-=1
        curr = curr.right
    return r