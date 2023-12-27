class Solution:
    def f(self, arr, pages):
        stud = 1
        nopages = 0
        for i in range(len(arr)):
            if nopages + arr[i] <= pages:
                nopages += arr[i]
                
            else:
                stud += 1
                nopages = arr[i]
                
        return stud
    
    #Function to find minimum number of pages.
    def findPages(self, arr, n, m):
        #code here
        if m > n:
            return - 1
            
        l,h = max(arr), sum(arr)
        
        while l <= h:
            mid = (l + h) // 2
            
            if self.f(arr, mid) > m:
                l = mid + 1
                
            else:
                h = mid - 1
                
        return l
        
