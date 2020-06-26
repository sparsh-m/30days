#https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        hash_map = {}
        while curr:
            hash_map[curr]=Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                hash_map[curr].next = hash_map[curr.next]
            if curr.random:
                hash_map[curr].random = hash_map[curr.random]
            curr = curr.next
        
        return hash_map[head] if head else head
