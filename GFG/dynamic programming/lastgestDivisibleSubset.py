class Solution:
    
    def LargestSubset(self, n, arr):
        #Code here
        dp = [1] * n
        hash = [0] * n
        maxi = 1
        lastOccur = 0
        arr.sort()
        
        for ind in range(n):
            hash[ind] = ind
            for prev in range(ind):
                if arr[ind] % arr[prev] == 0 and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    hash[ind] = prev
                    
            if dp[ind] > maxi:
                maxi = dp[ind]
                lastOccur = ind
                
        lds = [0] * maxi
        lds[0] = arr[lastOccur]
        ind = 1
        
        while hash[lastOccur] != lastOccur:
            lastOccur = hash[lastOccur]
            lds[ind] = arr[lastOccur]
            ind += 1
            
        lds.reverse()
        
        return lds
