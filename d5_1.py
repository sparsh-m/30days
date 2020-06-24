#https://www.geeksforgeeks.org/reverse-a-linked-list/
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
	prev=None
	curr=head
	while curr:
		next=curr.next
		curr.next=prev
		prev=curr
		curr=next
	head=prev
	return head

def traverse(n):
	temp = n
	while(temp.next):
		print(temp.val)
		temp=temp.next
	print(temp.val)



d = ListNode(4)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

traverse(a)
q = reverseList(a)
traverse(q)


