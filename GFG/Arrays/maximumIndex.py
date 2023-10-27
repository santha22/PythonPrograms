class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self, arr, n): 
        ##Your code here 
        rightMax = [0] * n    
        leftMin = [0] * n     
        
        Max = arr[n - 1]
        Min = arr[0]
        
        # array for maintain rightMaximum
        for i in range(n - 1, -1, -1):
            if Max < arr[i]:
                Max = arr[i]
                
            rightMax[i] = Max
            
        # array for maintain leftMinimum
        for j in range(n):
            if Min > arr[j]:
                Min = arr[j]
                
            leftMin[j] = Min
        
        ans = 0
        i, j = 0, 0
        
        # find length of maximum index if leftMin[i] <= rightMax[j]
        while i < n and j < n:
            if leftMin[i] <= rightMax[j]:
                ans = max(ans, j - i)
                j += 1
                
            else:
                i += 1
        
        return ans
                
