class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def remove(head, n):
	curr=head
	#i will give number iof nodes + 1
	i=1
	while curr:
		curr = curr.next
		i+=1
	#gives position of to be deleted no de from front
	nfromfront = i-n
	if nfromfront == 1:
		head = head.next
	else:
		i=1
		curr = head
		while i<nfromfront-1:
			curr = curr.next
			i+=1
		
		curr.next = curr.next.next
	return head
	
#better solution but it isnt necesarrily a one pass
def remove2(head, n):
	dummy = ListNode()
	dummy.next = head
	first = dummy
	second = dummy
	i=0
	while i<n+1:
		first = first.next
		i+=1
		
	while first:
		first = first.next
		second = second.next
		
	second.next = second.next.next
	
	return dummy.next
	
