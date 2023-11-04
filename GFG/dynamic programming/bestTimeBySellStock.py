def maximumProfit(prices):
    # Write your code here.
    mini = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        val = prices[i] - mini
        profit = max(profit, val)
        mini = min(mini, prices[i])

    return profit
