class Solution:
    def f(self, a, b, c, ind, ind1, ind2, dp):
        if ind < 0 or ind1 < 0 or ind2 < 0:
            return 0
            
        if dp[ind][ind1][ind2] != -1:
            return dp[ind][ind1][ind2]
            
        if a[ind] == b[ind1] == c[ind2]:
            return 1 + self.f(a, b, c, ind - 1, ind1 - 1, ind2 - 1, dp)
            
        dp[ind][ind1][ind2] = max(self.f(a, b, c, ind - 1, ind1, ind2, dp), 
                    self.f(a, b, c, ind, ind1 - 1, ind2, dp),
                    self.f(a, b, c, ind, ind1, ind2 - 1, dp))
                    
        return dp[ind][ind1][ind2]

    def LCSof3(self, a, b, c,n1,n2,n3):
        # code here
        dp = [[[-1 for i in range(n3)] for i in range(n2)] for i in range(n1)]
        return self.f(a, b, c, n1 - 1, n2 - 1, n3 - 1, dp)
