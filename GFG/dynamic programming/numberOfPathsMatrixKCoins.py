
class Solution:
    
    def count_paths(self, arr, n, m, i, j, k, memo):
        if k < 0 or i < 0 or j < 0:
            return 0
            
        if i == 0 and j == 0:
            if k == arr[i][j]:
                return 1
                
            return 0
    
        if memo[i][j][k] != -1:
            return memo[i][j][k]
            
        left = self.count_paths(arr, n, m, i, j - 1, k - arr[i][j], memo)
        up = self.count_paths(arr, n, m, i - 1, j, k - arr[i][j], memo)
        
        memo[i][j][k] = left + up
        return memo[i][j][k]


    
    def numberOfPath (self, n, k, arr):
        # code here
        memo = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]
        return self.count_paths(arr, n, n, n - 1, n - 1, k, memo)
     
