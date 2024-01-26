class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        platNeed, result  = 1, 1
        i,j = 1, 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platNeed += 1
                i += 1
                
            elif arr[i] > dep[j]:
                platNeed -= 1
                j += 1
                
            result = max(result, platNeed)
            
        return result
