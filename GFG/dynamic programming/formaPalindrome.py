class Solution:
    
    def findMinInsertions(self, s):
        # code here
        s1 = s[::-1]
        n, m = len(s), len(s1)
        
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)
        
        for ind in range(1, n + 1):
            for ind1 in range(1, m + 1):
                if s[ind - 1] == s1[ind1 - 1]:
                    cur[ind1] = 1 + prev[ind1 - 1]
                    
                else:
                    cur[ind1] = max(prev[ind1], cur[ind1 - 1])
                    
            prev = cur[:]
        
        ans = prev[m]
        return n - ans
