#https://leetcode.com/problems/middle-of-the-linked-list/submissions/
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
import math

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#returns the position of the middle node
def countNodes(head):
	n=0
	curr=head
	while curr:
		curr=curr.next
		n+=1
	n = math.floor(n/2)+1
	return n		


def middleNode(head):
	mid=countNodes(head)
	i=1
	curr=head
	#less than mid as curr=curr.next threfore
	#one curr further is returned
	while i<mid:
		curr=curr.next
		i+=i
	return curr	

d = ListNode(4)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)
	
