class Solution:
    def subarraySumK(self, a : List[int] , n : int , k : int) -> int:
        ans = -1
        summ = 0
        l, r = 0, 0
        
        while r < n:
            summ = summ + a[r]
            
            while summ >= k:
                if ans == -1:
                    ans = r - l + 1
                    
                else:
                    ans = min(ans, r - l + 1)
                    
                summ = summ - a[l]
                l += 1
                
            r += 1
                
        return ans
