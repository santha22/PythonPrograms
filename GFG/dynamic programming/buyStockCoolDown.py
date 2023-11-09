class Solution:
        
    def maximumProfit(self, prices, n):
        #Code here
        dp = [[0] * (2) for i in range(n + 2)]
        
        
            
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                
                if buy == 1:
                    profit = max(-prices[ind] + dp[ind + 1][0], dp[ind + 1][1])
                    
                else:
                    profit = max(prices[ind] + dp[ind + 2][1], dp[ind + 1][0])
                    
                dp[ind][buy] = profit
                
        return dp[0][1]
