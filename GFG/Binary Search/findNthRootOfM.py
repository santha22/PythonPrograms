class Solution:
	def NthRoot(self, n, m):
		# Code here
		l,h = 1, m
		
		while l <= h:
		    mid = (l + h) // 2
		    
		    if mid ** n == m:
		        return mid
		        
		    elif mid ** n > m:
		        h = mid - 1
		        
		    elif mid ** n < m:
		        l = mid + 1
		        
		return -1
