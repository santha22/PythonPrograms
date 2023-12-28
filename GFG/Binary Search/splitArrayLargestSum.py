
class Solution:
    def f(self, arr, mid):
        count,  total = 1, 0
        for i in range(len(arr)):
            if total + arr[i] <= mid:
                total += arr[i]
                
            else:
                count += 1
                total = arr[i]
                
        return count
    
    def splitArray(self, arr, n, k):
        # code here 
        l,h = max(arr), sum(arr)
        while l <= h:
            mid = (l + h) // 2
            
            if self.f(arr, mid) > k:
                l = mid + 1
                
            else:
                h = mid - 1
                
        return l
