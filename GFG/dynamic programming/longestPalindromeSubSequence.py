class Solution:
    
    def longestPalinSubseq(self, s):
        # code here
        s1 = s[::-1]
        
        n, m = len(s), len(s1)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        
        for ind in range(1, n + 1):
            for ind1 in range(1, m + 1):
                if s[ind - 1] == s1[ind1 - 1]:
                    dp[ind][ind1] = 1 + dp[ind - 1][ind1 - 1]
                    
                else:
                    dp[ind][ind1] = max(dp[ind - 1][ind1], dp[ind][ind1 - 1])
                    
        return dp[n][m]
