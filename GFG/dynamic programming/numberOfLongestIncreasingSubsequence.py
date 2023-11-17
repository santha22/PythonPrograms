class Solution:
        
    
    def NumberofLIS(self, n, arr):
        # Code here
        dp = [1] * n
        count = [1] * n
        maxi = 1
        
        for ind in range(n):
            for prev in range(ind):
                if arr[ind] > arr[prev] and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    count[ind] = count[prev]
                    
                elif arr[ind] > arr[prev] and 1 + dp[prev] == dp[ind]:
                    count[ind] += count[prev]
                    
            maxi = max(maxi, dp[ind])
         
        nos = 0
        for i in range(n):
            if maxi == dp[i]:
                nos += count[i]
                
                
        return nos
