class Solution:
    def f(self, a, mid):
        count = 1
        total = 0
        for i in range(len(a)):
            if total + a[i] <= mid:
                total += a[i]
    
            else:
                total = a[i]
                count += 1
    
        return count
    
    def minTime (self, arr, n, k):
        #code here
        l,h = max(arr), sum(arr) 
        
        while l <= h:
            mid = (l + h) // 2
    
            if self.f(arr, mid)  > k:
                l = mid + 1
    
            else:
                h = mid - 1
    
        return l
        
