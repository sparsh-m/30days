#rod cutting
def rodCutting(profit, cutSize, total):
    dp = [[0 for i in range(total+1)] for i in range(len(profit))]
    for i in range(1, len(dp[0])):
        dp[0][i] = (i//cutSize[0])*profit[0]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if cutSize[i]<=j:
                dp[i][j] = max(dp[i-1][j], dp[i][j-cutSize[i]] + profit[i])
            else:
                dp[i][j] = dp[i-1][j]
    for i in dp:
        print(i)
        
profit = [2,5,7,8]
cutSize = [1,2,3,4]
rodCutting(profit, cutSize, 5)

 