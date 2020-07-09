#https://leetcode.com/problems/word-break/
"""
Will not work with python recursive
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checked = set()
        return self.dfs(s, wordDict, checked)

    def dfs(self, s, wordDict, checked):
        if not s:
            return True
        if s in checked:
            return False

        for w in  wordDict:
            if (s.startswith(w) and self.dfs(s[len(w):], wordDict, checked)):
                return True
        return False