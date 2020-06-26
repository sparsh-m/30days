#using hash table
def hasCycle(head):
	curr = head
	nodes = set()
	while curr:
		if curr not in nodes:
			nodes.add(curr)
		else:
			return True
		curr = curr.next
	return False

#using two pointers
def hasCycle2(head):
	dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
