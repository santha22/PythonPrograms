class Solution:
	def minJumps(self, arr, n):
	    #code here
	    totalJumps = 0
	    destination = n - 1
	    
	    coverage = lastJumpidx = 0
	    
	    if n == 1:
	        return 0
	    
	    for i in range(n):
	        coverage = max(coverage, i + arr[i])
	        
	        if i == lastJumpidx:
	            lastJumpidx = coverage
	            totalJumps += 1
	            
	            if coverage >= destination:
	                return totalJumps
	                
	    return -1
	            
