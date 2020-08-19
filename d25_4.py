#0/1 Knapsack 
#https://www.youtube.com/watch?v=8LusJS5-AGo
#TC = O(N^2)

def knapsack(weights, values, capacity):
    dp = [[0]*(capacity+1) for i in range(len(values))]
    for i in range(1, len(dp[0])):
        dp[0][i] = values[0]
    for i in range(1,len(weights)):
        for j in range(1,capacity+1):
            if weights[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(values[i] + dp[i-1][j-weights[i]], dp[i-1][j])
    for i in dp:
        print(i)
    return dp[-1][-1]

weights = [1,3,4,5]
values = [1,4,5,7]
capacity = 7
knapsack(weights, values, capacity)