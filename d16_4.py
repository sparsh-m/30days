#https://leetcode.com/problems/group-anagrams/
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    d = dict()
    for string in strs:
        #Each place representing an alphabet
        arr = [0]*26
        for j in string:
            #notes the occurence of each character
            #in an identifying array
            arr[ord(j)-97]+=1
        arr = tuple(arr)
        
        #insert the string in dictionary according to array
        if arr not in d:
            d[arr] = [string]
        else:
            d[arr].append(string)
    return d.values()