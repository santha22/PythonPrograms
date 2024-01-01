
class Solution:
    def maxChildren(self, n, m, g, s):
        # Code here
        count = 0
        i,j = 0,0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            while j < len(s) and g[i] > s[j]:
                j += 1
                
            if j < len(s) and g[i] <= s[j]:
                count += 1
                
                i += 1
                j += 1
                
        return count
