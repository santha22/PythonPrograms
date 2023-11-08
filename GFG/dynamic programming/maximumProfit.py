
class Solution:

    
    def maxProfit(self, k, n, arr):
        # code here
        dp = [[0] * ((2 * k) + 1) for i in range(n + 1)]
        
        for ind in range(n - 1, -1, -1):
            for trans in range((2 * k) - 1, -1, -1):
                profit = 0
                if trans % 2 == 0:
                    profit = max((-arr[ind] + dp[ind + 1][trans + 1]), dp[ind + 1][trans])
                    
                else:
                    profit = max((arr[ind] + dp[ind + 1][trans + 1]), dp[ind + 1][trans])
                    
                dp[ind][trans] = profit
                
        return dp[0][0]
