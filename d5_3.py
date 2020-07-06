#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#iterative TC: O(n) SC: O(n)
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

#iterative, in place TC: O(n) SC: O(1)
def mergeInPlace(l1, l2):
	if not l1 and not l2:
		return l1 or l2
	dummy = curr = ListNode(0)
	dummy.next = l1
	while l1 and l2:
		if l1.val<l2.val:
			l1 = l1.next
		else:
			#read here
			nxt = curr.next
			temp = l2.next
			curr.next = l2
			l2.next = nxt
			l2 = temp
		curr = curr.next
	#if l2 is left we append it to the end of the given linked list
	if l2:
		curr.next = l2
	
	return dummy.next