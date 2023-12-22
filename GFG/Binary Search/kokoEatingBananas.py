import math
class Solution:
    def calculate(self, piles, n, mid):
        totalH = 0
        # Find total hours
        for i in range(n):
            totalH += math.ceil(piles[i] / mid)
        return totalH
            
            
    def Solve(self, n, piles, H):
        # Code here
        
        l = 1
        h = max(piles)
        
        while l <= h:
            mid = (l + h) // 2
            total = self.calculate(piles, n, mid)
            
            if total <= H:
                h = mid - 1
                
            else:
                l = mid + 1
                
        return l
                
