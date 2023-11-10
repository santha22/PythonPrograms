
class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        # Code here
        dp = [1] * n
        maxi = 1
        lastOccur = 0
        hash = [0] * n
        
        for ind in range(n):
            hash[ind] = ind
            for prev in range(ind):
                if arr[prev] < arr[ind] and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    hash[ind] = prev
                    
            if dp[ind] > maxi:
                maxi = dp[ind]
                lastOccur = ind
                
        
                
        lis = [0] * maxi
        lis[0] = arr[lastOccur]
        ind = 1
        
        while hash[lastOccur] != lastOccur:
            lastOccur = hash[lastOccur]
            lis[ind] = arr[lastOccur]
            ind += 1
            
        lis.reverse()
        
        return lis
