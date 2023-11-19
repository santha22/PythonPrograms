class Solution:
    
        
    def matrixMultiplication(self, n, arr):
        # code here
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
        
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n):
                if i == j:
                    continue
                
                else:
                    mini = 1e9
                    for k in range(i, j):
                        steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]
                        
                        mini = min(mini, steps)
                        
                    dp[i][j] = mini
                
        return dp[1][n - 1]
