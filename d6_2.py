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
		
#space and time is O(N)	
#def isPalindrome(self, head: ListNode) -> bool:
#        vals = []
#        while head:
#            vals.append(head.val)
#            head = head.next
#        return vals == vals[::-1]

def pal(head):
	slow = head
	fast = head
	
	if not head:
		return True
	#corner cases when len=1 or len=2
	if head.next == None:
		return True
	elif head.next.next == None:
		if head.val == head.next.val:
			return True
		else:
			return False
	
	#for lengths n>=3
	while fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
	
	prev = None
	curr = slow
	while curr:
		nextt = curr.next
		curr.next = prev
		prev = curr
		curr = nextt
	
	revhead = prev
	flag = True
	while head and revhead:
		if head.val != revhead.val:
			flag = False
			break
		head = head.next
		revhead = revhead.next
	print(flag)
	return flag
head = makeList([1,2,3,3,2,1])
pal(head)
