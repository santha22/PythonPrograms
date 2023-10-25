class Solution:
    
	def maxSumIS(self, arr, n):
		# code here 
		next = [0]*(n + 1)
		cur = [0]*(n + 1)
		
		for ind in range(n - 1, -1, -1):
		    for prev in range(ind - 1, -2, -1):
		        nottake = next[prev + 1]
		        
		        take = 0
		        if prev == -1 or arr[ind] > arr[prev]:
		            take = arr[ind] + next[ind + 1]
		           
		        cur[prev + 1] = max(nottake, take)
		       
		    next, cur = cur, next
		        
	    return next[-1 + 1]
