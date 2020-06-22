#https://leetcode.com/problems/longest-substring-without-repeating-characters/
def solve(s):
    n = len(s)
    i=0
    j=0
    ans=0
    hash_map={}
    while(i<n and j<n):
        if s[j] not in hash_map:
            hash_map[s[j]]=j
            j+=1
            ans=max(ans,j-i)
        else:
            i=max(hash_map[s[j]]+1,i)
            del hash_map[s[j]]
    return ans
s="abcdaenv"
print(solve(s))
