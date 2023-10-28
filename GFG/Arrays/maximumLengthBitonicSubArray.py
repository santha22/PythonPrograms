class Solution:

    def bitonic(self,arr, n):
        # code here
        if n == 0:
            return 0
            
        maxi = 1
        start = 0
        nextStart = 0
        
        j = 0
        while j < n - 1:
            while j < n - 1 and arr[j] <= arr[j + 1]:
                j = j + 1
                
            while j < n - 1 and arr[j] >= arr[j + 1]:
                if j < n - 1 and arr[j] > arr[j + 1]:
                    nextStart = j + 1
                    
                j = j + 1
                
            maxi = max(maxi, j - (start - 1))
            
            start = nextStart
            
        return maxi
