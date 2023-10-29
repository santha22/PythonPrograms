class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        
         #code here
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for ind in range(1, m + 1):
            for ind1 in range(1, n + 1):
                if X[ind - 1] == Y[ind1 - 1]:
                    dp[ind][ind1] = 1 + dp[ind - 1][ind1 - 1]
                    
                else:
                    dp[ind][ind1] = max(dp[ind - 1][ind1], dp[ind][ind1 - 1])
        ans = dp[m][n]
        ans = (m - ans) + (n - ans) + ans
        
        return ans
