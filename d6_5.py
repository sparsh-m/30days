#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
         
class Solution:
    def endnode(self,head):
        prev = None
        curr = head
        while curr:
            prev = curr
            curr = curr.next
        return prev
    
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            next = curr.next
            if curr.child:
                below = curr.child
                curr.next = below
                
                belowend = self.endnode(below)
                below.prev = curr
                curr.child = None
                belowend.next = next
                if next:
                    next.prev = belowend
                curr = below
            else:
                curr = curr.next
        return head
