#https://leetcode.com/problems/binary-search-tree-iterator/submissions/
def __init__(self, root):
        self.stack = []
        self.leftmost(root)
    
    def leftmost(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp  = self.stack.pop()
        if temp.right:
            self.leftmost(temp.right)
        return temp.val
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        return False
