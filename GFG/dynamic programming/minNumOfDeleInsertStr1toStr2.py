class Solution:
    def f(self, ind, ind1, s, t, dp):
        if ind == 0 or ind1 == 0:
            return 0
            
        if dp[ind][ind1] != -1:
            return dp[ind][ind1]
        
        if s[ind - 1] == t[ind1 - 1]:
            dp[ind][ind1] = 1 + self.f(ind - 1, ind1 - 1, s, t, dp)
            return dp[ind][ind1]
            
        dp[ind][ind1] = max(self.f(ind - 1, ind1, s, t, dp), self.f(ind, ind1 - 1, s, t, dp))
            
        return dp[ind][ind1]
    
	def minOperations(self, s1, s2):
		# code here 
		n = len(s1)
		m = len(s2)
		
		dp = [[-1] * (m + 1) for i in range(n + 1)]
		ans = self.f(n, m, s1, s2, dp)
		
		return n + m - (2 * ans)
