class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		prev = arr[0]
		prev2 = 0
		for i in range(1, n):
		    nottake = prev
		    take = arr[i]
		    if i > 1:
		        take += prev2
		    
		    cur = max(nottake, take)
		    prev2 = prev
		    prev = cur
		
		return prev
