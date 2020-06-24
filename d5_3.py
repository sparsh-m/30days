#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeList(l1,l2):
	a=l1
	b=l2
	c=ListNode()
	head = c
	while a and b:
		if a.val<=b.val:
			c.next = ListNode(a.val)
			c = c.next
			a = a.next
		else:
			c.next = ListNode(b.val)
			c = c.next
			b = b.next
	
	while a:
		c.next = ListNode(a.val)
		c = c.next
		a = a.next
	
	while b:
		c.next = ListNode(b.val)
		c = c.next
		b = b.next
	
	return head
	
