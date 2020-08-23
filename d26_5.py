def eggsolve(floor, egg):
    dp = [[0 for i in range(egg+1)]for i in range(floor+1)]

    for i in range(floor+1):
        dp[i][1] = i
    for i in range(egg+1):
        dp[1][i] = 1

    for i in range(2, floor+1):
        for j in range(2, egg+1):
            dp[i][j] = 1000000
            for x in range(1, i):
                brokenEggResult = dp[x-1][j-1]
                eggSurvivedResult = dp[i-x][j]
                temp = max(brokenEggResult, eggSurvivedResult)+1
                if temp<dp[i][j]:
                    dp[i][j] = temp
    
    return dp[-1][-1]

floor =14 
egg =3

eggsolve(floor, egg)