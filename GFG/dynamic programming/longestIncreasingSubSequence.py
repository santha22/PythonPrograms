class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp = [[0] * (n + 1) for i in range(n + 1)]
		
		for ind in range(n - 1, -1, -1):
		    for prev in range(ind - 1, -2, -1):
		        nottake = dp[ind + 1][prev + 1]
		        
		        take = 0
		        if prev == -1 or a[ind] > a[prev]:
		            take = 1 + dp[ind + 1][ind + 1]
		           
		        dp[ind][prev + 1] = max(nottake, take)
		        
	    return dp[0][-1 + 1]
