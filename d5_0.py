class Node:
	def __init__(self, val=None,next=None):
		self.val=val
		self.next=next
	
	def __str__(self):
		return str(self.val)

d = Node(4)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)

def traverse(n):
	temp = n
	while(temp.next):
		print(temp)
		temp=temp.next
	print(temp)
		
traverse(a)


