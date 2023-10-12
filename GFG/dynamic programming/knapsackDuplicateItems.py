class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[0] * (W + 1) for i in range(N)]
        
        for t in range(W + 1):
            dp[0][t] = (t // wt[0]) * val[0]
            
        for i in range(1, N):
            for j in range(W + 1):
                nottake = 0 + dp[i - 1][j]
                
                take = 0
                if wt[i] <= j:
                    take = val[i] + dp[i][j - wt[i]]
                    
                dp[i][j] = max(take, nottake)
                
        return dp[N-1][W]
