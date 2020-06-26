#https://leetcode.com/problems/rotate-list/submissions/
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None:
            return head
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        if k==0 or k%length==0:
            return head
        k = k%length
        first = head
        second = head
        i=0
        while i<k:
            i+=1
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        
        first.next = head
        head = second.next
        second.next = None
        
        return head
