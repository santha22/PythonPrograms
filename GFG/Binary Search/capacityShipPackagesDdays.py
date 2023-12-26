class Solution:
    def f(self, arr, n, mid):
        days, load = 1, 0
        for i in range(n):
            if load + arr[i] > mid:
                days += 1
                load = arr[i]
                
            else:
                load += arr[i]
                
        return days
    
    def leastWeightCapacity(self, arr, n, d):
        # code here 
        l,h = max(arr), sum(arr)
        while l <= h:
            mid = (l + h) // 2
            
            if self.f(arr, n, mid) <= d:
                h = mid - 1
                
            else:
                l = mid + 1
                
        return l
