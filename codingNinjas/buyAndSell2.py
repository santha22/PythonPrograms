
def getMaximumProfit(values, n) :
	#Your code goes here
    if n == 0:
        return 0
    
    dp = [[0 for i in range(2)] for i in range(n + 1)]
    dp[n][0] = dp[n][1] = 0
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            if buy == 1:
                profit = max((-values[ind] + dp[ind + 1][0]), dp[ind + 1][1])

            else:
                profit = max((values[ind] + dp[ind + 1][1]), dp[ind + 1][0])

            dp[ind][buy] = profit

    return dp[0][1]
