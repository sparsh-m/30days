#https://leetcode.com/problems/palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.backtrack(s,[],res)
        return res
    
    def isPal(self,s):
        return s==s[::-1]
    
    def backtrack(self,s,path,res):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if self.isPal(s[:i]):
                self.backtrack(s[i:],path+[s[:i]],res)
    
