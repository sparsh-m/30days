#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/
#Time Complexity: O(N)
#Space Complexity
#The prev increases the dept and curr traverses across the level
#from left to right
#TreeNode has an extra pointer of next
def connect(self, root: 'Node') -> 'Node':
    if not root:
        return root
    prev = root
    curr = None
    while prev.left:
        curr = prev
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        prev = prev.left
    return root