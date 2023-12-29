import math
class Solution:
    def f(self, arr, dist, n):
        
        cnt = 0
        
        for i in range(n - 1):
            cnt += math.floor((arr[i + 1] - arr[i]) / dist)
            
        return cnt
    
    def findSmallestMaxDist(self, arr, k):
        # Code here
        n = len(arr)
        l,h = 0,0
        for i in range(n - 1):
            h = max(h, arr[i + 1] - arr[i])
            
        while h - l > 1e-6:
            mid = (l + h) / 2.0
            
            if self.f(arr, mid, n) > k:
                l = mid 
                
            else:
                h = mid
                
        return round(h, 2)
