#https://leetcode.com/problems/intersection-of-two-linked-lists/
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""
1)Suppose len a is 4 and b is 3 with intersection at point 3
after two iterations by both pointers both have covered 4+3 nodes
therefore if the nodes connect they will meet.
2)1)In case of no intersection the loop will still terminate
as for the last iter a.next and b.next will be null.
TC: O(n)
SC: O(1)
"""

def getIntersectionNode(headA, headB):
	a = headA; b = headB
	while a!=b:
		a = a.next if a else headB
		b = b.next if b else headA
	return a
