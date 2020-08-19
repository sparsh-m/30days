#https://leetcode.com/problems/longest-common-subsequence
"""
Time, Space Complexity: O(nm)
"""
#run program to see dp table
#besides the length you can also find the subsequence
def solve(text1, text2):
    dp = [[0]*(len(text1)+1) for i in range(len(text2)+1)]
    for i in range(0, len(text2)):
        for j in range(0, len(text1)):
            if text1[j]==text2[i]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    for i in dp:
        print(i)
    print(len(text1), len(text2))
    print(len(dp[0]), len(dp))
    return dp[-1][-1]

a = solve("bsbininm","jmjkbkjkv")
print(a)