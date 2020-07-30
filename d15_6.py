#Rabin Karp for string matching
"""
Given a pattern "abc", we take a prime no for eg 101,
and calculate the hash function as such,
ord(a)*(**0) + ord(b)*(**1) + ord(c)*(**2)

Now the hash of the text string is cakculated, with number of characters
in pattern at a time it the hash value of the pattern and substring matches then
strings are compared.
Time Complexity:O(N*M)
N length of text, M length of pattern
This happens if we a have a bad hash function and all the hash value come out to be the same
"""
def rabinkarp(text, pattern):
    prime = 3
    n = len(text)
    m = len(pattern)
    patternHash = calculateHash(pattern, prime)
    textHash = calculateHash(text[0:m],prime)

    print(textHash, patternHash)
    if patternHash == textHash:
        if text[:m] == pattern:
            return 0

    for i in range(m,n):
        print(text[i-m:i+1], pattern)
        textHash = newHash(textHash, text[i-m:i+1], prime, m)
        print(textHash, patternHash)
        if patternHash == textHash:
            if text[i-m+1:i+1] == pattern:
                return text[i-m+1:i+1]

def calculateHash(s, prime):
    hashVal = 0
    for i in range(len(s)):
        hashVal+=(ord(s[i])*(prime**i))
    return hashVal

def newHash(oldHash, s, prime, m):
    oldHash -= ord(s[0])
    oldHash//=prime
    oldHash += ord(s[-1])*(prime**(m-1))
    return oldHash

prime = 3
text = "abcd"
pattern = "bcdd"


def solution(text, pattern):
    t = 0
    p = 0
    m = len(pattern)
    n = len(text)
    prime=3
    flag = 0 
    for i in range(m):
        p+=(ord(pattern[i])*(prime**i))
    
    #First Window
    for i in range(m):
        t+=(ord(text[i])*(prime**i))
    
    if t==p:
        for i in range(m):
            if text[i] != pattern[i]:
                flag = 1
                break
        if not flag:
            return 0
    
    for i in range(m,n):
        flag = 0
        #calculating newhash
        t -= ord(text[i - m])
        t//=prime
        t += (ord(text[i])*(prime**(m-1)))

        if t==p:
            for j in range(m):
                #print(text[i-m+1] , pattern[j])
                if text[i-m+j+1] != pattern[j]:
                    flag = 1
                    break
            if not flag:
                return i-m+1
    return -1

text = "c"
pattern = "cc"
res = solution(text, pattern)
print(res)