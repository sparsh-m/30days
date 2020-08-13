#https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/

class Node: 
    def __init__(self, key): 
        self.key  = key 
        self.left = None
        self.right = None

def insert(node , key): 
    if node is None: 
        return Node(key) 
  
    if key < node.key: 
        node.left = insert(node.left, key) 
  
    else: 
        node.right = insert(node.right, key) 
  
    return node

root = None
root = insert(root, 50) 
insert(root, 30); 
insert(root, 20); 
insert(root, 40); 
insert(root, 70); 
insert(root, 60); 
insert(root, 80); 

pre = 0
suc = 0
key = 65
def finPreSuc(root, key):
    if not root:
        return

    if root.key == key:

        if root.left:
            temp = root.left
            while temp.right:
                temp=temp.right
            finPreSuc.pre = temp.key
        
        if root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            finPreSuc.suc = temp.key
        
        return temp
    
    if root.key<key:
        finPreSuc.pre = root.key
        finPreSuc(root.right,key)
    if root.key>key:
        finPreSuc.suc = root.key
        finPreSuc(root.left, key)
findPreSuc.pre = None
findPreSuc.suc = None
        
    
finPreSuc(root, key)
print(finPreSuc.pre, finPreSuc.suc)
