#https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/
def deleteNode(node):
        """
        1 2 3 4
        1 3 3 4
          |   ^       
          |___|   
        1 3 4
        """
        node.val = node.next.val
        node.next = node.next.next
