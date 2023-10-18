#User function template for Python

class Solution:    
    def remove_duplicate(self, arr, n):
        # code here
        for i in range(n - 1, -1, -1):
            if arr[i] == arr[i - 1] and i > 0:
                
                arr.pop(i)
          
        return len(arr)
                
        
