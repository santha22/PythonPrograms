class Solution:
    def f(self, stalls, cows, dist):
        countCows = 1
        n = len(stalls)
        last = stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= dist:
                countCows += 1
                last = stalls[i]
                
            if countCows >= cows:
                return True
                
        return False
        
        
    def solve(self,n,k,stalls):
        stalls.sort()
        
        l,h = 1, stalls[n - 1] - stalls[0]
        
        while l <= h:
            mid = (l + h) // 2
            
            if self.f(stalls, k, mid):
                l = mid + 1
                
            else:
                h = mid - 1
                
        return h
