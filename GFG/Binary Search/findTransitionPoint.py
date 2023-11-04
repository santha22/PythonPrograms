class Solution:
    def transitionPoint(self, arr, n): 
        # Code here 
        if n == 1 and arr[0] == 1:
            return 0
            
        
            
        first = -1
        l, h = 0, n - 1
        while l < h:
            mid = (l + h) // 2
            
            if arr[mid] == 1:
                first = mid
                h = mid
                
            if arr[mid] < 1:
                l = mid + 1
                
        return first
