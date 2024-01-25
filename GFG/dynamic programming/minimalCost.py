class Solution:
    
    def minimizeCost(self, height, n, k):
        dp = [0] * n
        
        for ind in range(1, n):
            minSteps = 1e9
            for i in range(1, k + 1):
                if ind - i >= 0:
                    jump = abs(height[ind] - height[ind - i]) + dp[ind - i]
                    minSteps = min(jump, minSteps)
                
            dp[ind] = minSteps
            
        return dp[n - 1]
