class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0] * (m + 1) for i in range(n + 1)]
        ans = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                    
                else:
                    dp[i][j] = 0
                    
        return ans

