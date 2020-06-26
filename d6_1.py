class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
	a = headA; b = headB
	# in case of no intersection
	# the loop will still terminate
	# as  as for the last iter a.next and
	# b.next will be null
	while a!=b:
		a = a.next if a else headB
		b = b.next if b else headA
	return a
