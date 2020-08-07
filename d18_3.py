#https://leetcode.com/problems/diameter-of-binary-tree/
def diameter(root):
    if not root:
        return 0
    self.ans = 0
    def depth(root):
        if not root:
            return 0
        L = depth(root.left)
        R = depth(root.right)
        #adds both arms of a node to give the diameter
        self.ans = max(L+R+1, self.ans)
        #passes on the length of the longer arm to it's parent
        return max(L,R)+ 1
    
    depth(root)
    #diameter is measured in edges not nodes
    return self.ans-1