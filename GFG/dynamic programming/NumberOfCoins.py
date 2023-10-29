class Solution:
    
    def minCoins(self, coins, M, V):
        # code here
        dp = [[0] * (V + 1) for i in range(M)]
        
        for i in range(V + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
               
            else:
                dp[0][i] = 1e9 
                
        for ind in range(1, M):
            for target in range(V + 1):
                nottake = dp[ind - 1][target]
                take = 1e9
                
                if coins[ind] <= target:
                    take = 1 + dp[ind][target - coins[ind]]
                   
                dp[ind][target] = min(nottake, take)
                
        ans = dp[M - 1][V]
        
        if ans >= 1e9:
            return - 1
            
        return ans
        
