#https://leetcode.com/problems/lru-cache/
"""
All the operations take O(1) time
"""
class Node:
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None
class LRUCache:
    #inititates a doubly linked list#
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        #If the key is present in the dictionary 
        #let n be the corrsponding node
        # _remove from the doubly linked list
        # and place it in the back#
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
        
    def put(self, key, value):
        #Adds an element to the back, always
        # Removes the element from prev position in the
        # linked if it was already there#
        if key in self.dic.keys():
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        #Adding the element to the dictionary
        self.dic[key] = n

        #If the capacity of cache is exceeded,
        #element in the front is deleted to compensate#
        if self.capacity < len(self.dic):
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
        
    def _add(self,n):
        #Adds a new node to the back of 
        #the array#
        p = self.tail.prev
        
        p.next = n
        n.prev = p

        n.next = self.tail
        self.tail.prev = n
    
    def _remove(self,n):
        #Removes an element by bypassing it#
        p = n.prev
        nxt = n.next

        p.next = nxt
        nxt.prev = p
