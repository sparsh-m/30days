class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
def detectCycle(head):
    if head==None or head.next == None:
		return None
    slow = head
    fast = head
    flag = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
			meetingNode = slow
			flag =  True
			break
    if flag:
		start = head
		while start != meetingNode:
			start = start.next
			meetingNode = meetingNode.next
		return meetingNode
    
a = ListNode(1)
b = ListNode(3)
c = ListNode(2)
d = ListNode(4)

a.next=b
b.next=c
c.next=d
d.next=b

node = detectCycle(a)
if node:
	print(node.val)
