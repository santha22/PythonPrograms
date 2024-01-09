import sys

class Solution:
        
    def upper_bound(self, arr, x, n):
        low, high = 0, n - 1
        ans = n
        while low <= high:
            
            mid = (low + high) // 2
            if arr[mid] > x:
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return ans
    
    def count_small_equal(self, matrix, n, m, x):
        cnt = 0
        for i in range(n):
            cnt += self.upper_bound(matrix[i], x, m)
            
        return cnt
    
    def median(self, matrix, r, c):
    	#code here 
    	low = sys.maxsize
    	high = -sys.maxsize
    	n = len(matrix)
    	m = len(matrix[0])
    	
    	for i in range(n):
    	    low = min(low, matrix[i][0])
    	    high = max(high, matrix[i][m-1])
    	    
    	req = (n * m) // 2
    	while low <= high:
    	    mid = (low + high) // 2
    	    small = self.count_small_equal(matrix, n, m, mid)
    	    
    	    if small <= req:
    	        low = mid + 1
    	        
    	    else:
    	        high = mid - 1
    	        
    	return low
