"""
author:sparsh-misra
version:3.7
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def makeList(arr):
	dummy = ListNode(0)
	curr = dummy
	for i in arr:
		curr.next = ListNode(i)
		curr = curr.next
	return dummy.next

def traverse(head):
	curr = head
	while curr:
		print (curr.val)
		curr = curr.next

def reverseKGroup(head, k):
	length=0
	count = head
	while count:
		length+=1
		count = count.next
	dummy = ListNode(0)
	dummy.next = head
	tether = dummy
	curr = head
	n=0
	i=0
	while curr and i<length//k:
		i+=1
		prev = None
		superprev = curr
		n=0
		while n<k:
			n+=1
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		tether.next = prev
		tether = superprev
	#incase of left over nodes
	if length % k != 0:
		tether.next = curr
	return dummy.next

arr = [1,2,3,4,5,6]
head = makeList(arr)
newhead = reverseKGroup(head, 3)
traverse(newhead)
		