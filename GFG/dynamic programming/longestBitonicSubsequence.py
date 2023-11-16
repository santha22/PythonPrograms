class Solution:
        
	def LongestBitonicSequence(self, nums):
		# Code here
		n = len(nums)
        dp1 = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp1[j] > dp1[i]:
                    dp1[i] = 1 + dp1[j]
               
		
		dp2 = [1] * n
		n = len(nums)
        dp2 = [1] * (n) 
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, - 1):
                if nums[i] > nums[j] and 1 + dp2[j] > dp2[i]:
                    dp2[i] = 1 + dp2[j]
                    
    
		maxi = 0
		
		for i in range(len(nums)):
		    maxi = max(maxi, dp1[i] + dp2[i] - 1)
		    
		return maxi
