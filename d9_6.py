#https://leetcode.com/problems/word-break/
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        return self.helper(s,wordDict,"",visited)
    
    def helper(self,s,wordDict,string,visited):
        if string==s:
            return True
        for i in range(len(wordDict)):
            if i not in visited:
                visited.add(i)
                self.helper(s,WordDict,string+wordDict[i],visited)
                visited.remove(i)
"""
def wordBreak(s,wordDict):
    visited = set()
    return helper(flag,s,wordDict,"",visited)

def helper(s,wordDict,string,visited):
	if string==s:
		return True
	for i in range(len(wordDict)):
		if i not in visited:
			visited.add(i)
			if helper(s,wordDict,string+wordDict[i],visited):
				return True
			visited.remove(i)
	return False
r = wordBreak("ba",["a","b"])
print(r)
