class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
        prefix = 1
        sufix = 1
        maxi = float("-inf")
        n = len(arr)
        for i in range(n):
            if prefix == 0:
                prefix = 1
                
            if sufix == 0:
                sufix = 1
                
            prefix = prefix * arr[i]
            sufix = sufix * arr[n - i - 1]
                
            maxi = max(maxi, max(prefix, sufix))
        
        return maxi
