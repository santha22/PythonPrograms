class Solution: 
    
    def sequenceCount(self,arr1, arr2):
        # Code here
        n, m = len(arr1), len(arr2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        mod = (10 ** 9) + 7
        
        for ind1 in range(n + 1):
            dp[ind1][0] = 1
            
        
            
        for ind in range(1, n + 1):
            for ind1 in range(1, m + 1):
                if arr1[ind - 1] == arr2[ind1 - 1]:
                    dp[ind][ind1] = (dp[ind - 1][ind1 - 1] + dp[ind - 1][ind1]) % mod
                    
                else:
                    dp[ind][ind1] = dp[ind - 1][ind1]
                    
        return dp[n][m]
