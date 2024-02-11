class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        xcount, ycount = 0, 0
        for i in range(n):
            if arr[i] == x:
                xcount += 1
                
            if arr[i] == y:
                ycount += 1
                
        if xcount > ycount:
            return x
        
        elif ycount > xcount:
            return y
            
        return min(x, y)
  
  
