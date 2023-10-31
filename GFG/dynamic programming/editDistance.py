class Solution:
            
    
    def editDistance(self, s, t):
        # Code here
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        
        for ind1 in range(m + 1):
            dp[0][ind1] = ind1
            
        for ind in range(n + 1):
            dp[ind][0] = ind
            
            
        for ind in range(1, n + 1):
            for ind1 in range(1, m + 1):
                if s[ind - 1] == t[ind1 - 1]:
                    dp[ind][ind1] = dp[ind - 1][ind1 - 1]
                    
                else:
                    dp[ind][ind1] = 1 + min(dp[ind - 1][ind1 - 1], 
                                            dp[ind - 1][ind1], 
                                            dp[ind][ind1 - 1])
                                            
        return dp[n][m]
