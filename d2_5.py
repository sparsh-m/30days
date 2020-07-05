#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
"""
Time Complexity:O(n)
Space Complexity:O(1)
"""
def maxProfit(prices):
    i=0
    profit=0
    if not prices:
        return 0
    buyval = prices[0]
    for i in range(1, len(prices)):
        temp = prices[i]-buyval
        profit = max(profit, temp)
        buyval = min(buyval, prices[i])
    return profit

print(maxProfit([7,6,4,3,100]))