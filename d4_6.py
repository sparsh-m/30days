#https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
1)Define two pointers i and j, j+1-i will give length of
the current non repeating substring.
2)If arr[j] is not in hash table save it and its index, and update max_len.
3)If arr[j] is in the hash table, i = max(i, hash_table[arr[j]]+1) 
and delete arr[j] from hash table.

"""
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
