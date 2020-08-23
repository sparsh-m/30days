def wordbreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in range(len(s)+1):
        for j in range(i):
            if not dp[j]:
                continue
            if s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[len(s)]

wordDict = [
    'i',
    'am',
    'a',
    'ace'
]

s = 'iamace'
print(wordbreak(s, wordDict))