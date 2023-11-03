class Solution:
        
    def f(self, i, j, pattern, string, dp):
        if i < 0 and j < 0:
            return True
            
        if i < 0 and j >= 0:
            return False
            
        if j < 0 and i >= 0:
            for it in range(i):
                if pattern[it] != "*":
                    return False
            
            return True
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        if pattern[i] == string[j] or pattern[i] == "?":
            dp[i][j] = self.f(i - 1, j - 1, pattern, string, dp)
            return dp[i][j]
            
        if pattern[i] == "*":
            dp[i][j] = self.f(i - 1, j, pattern, string, dp) or self.f(i, j - 1, pattern, string, dp)
            return dp[i][j]
            
        return False
    
    def wildCard(self,pattern, string):
        # Code here
        n, m = len(pattern), len(string)
        
        dp = [[-1] * (m) for i in range(n)]
        
        return self.f(n - 1, m - 1, pattern, string, dp)
