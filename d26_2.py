#Coin Change
#https://leetcode.com/problems/coin-change/submissions/
def findseq(dpseq, coins):
    res=[]
    total = len(dpseq)-1
    currCoin = coins[dpseq[-1]]
    while total>0:
        total-=currCoin
        res.append(currCoin)
        currCoin = coins[dpseq[total+1]]
    return res

def coinChange(coins, total):
    dp = [10000]*(total+1)
    dpSeq = [-1]*(total+1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(1,total+1):
            if j>=coins[i]:
                if dp[j]>dp[j-coins[i]]+1:
                    dp[j] = dp[j-coins[i]]+1
                    dpSeq[j] = i
    print(findseq(dpSeq, coins))
    print(dp, dpSeq)



coins = [7,2,3,6]
coinChange(coins, 13)