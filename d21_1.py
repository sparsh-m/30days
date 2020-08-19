#https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/
class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def ceil(root, key):
    if not root:
        return 0
    
    if root.key == key:
        return root.key

    if root.key<key:
        return ceil(root.right, key)
    
    val =  ceil(root.left, key)
    return val if val>=key else root.key

def floor(root, key):
    if not root:
        return 100
    
    if root.key==key:
        return root.key
    
    if root.key>key:
        return floor(root.left, key)
    
    val = floor(root.right, key)
    return val if val<=key else root.key
root = TreeNode(4) 
  
root.left = TreeNode(1) 
root.right = TreeNode(6) 

print(ceil(root, 3))
print(floor(root, 5))