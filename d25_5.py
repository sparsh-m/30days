#https://leetcode.com/problems/edit-distance
#TC, SC = O(n*m)

def solve(word1, word2):
    dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
    for i in range(1,len(dp[0])):
        dp[0][i] = i
    
    for i in range(1, len(dp)):
        dp[i][0] = i
    #main logic
    for j in range(1, len(dp[0])):
        for i in range(1, len(dp)):
            #if alphabet same don't have to change
            #(ab, db) need the same number of swaps as (a,d)
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                #pick the min swaps around and add 1
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    for i in dp:
        print(i)
    return dp[-1][-1]

solve('ros','horse')