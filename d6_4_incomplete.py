#https://leetcode.com/problems/linked-list-cycle/
#TC: O(n)
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#using hash table
def hasCycle(head):
	curr = head
	#Maintains a set of visited nodes
	#and returns true if a node is already
	#in the set, ie already visited
	nodes = set()
	while curr:
		if curr not in nodes:
			nodes.add(curr)
		else:
			return True
		curr = curr.next
	return False

#using two pointers
#SC: O(1)
def hasCycle2(head):
	#Add a dummy node to the beginning of the array
	dummy = ListNode(0)
	dummy.next = head
	#Slow pointer moves one step at a time
	#fast pointer moves two steps at a time
	slow = dummy
	fast = dummy
	#If a loop is present slow and fast will
	#point to the same element, since fast is in
	#the second lap and slow in the first
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False
