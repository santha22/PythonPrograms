#User function Template for python3
from collections import defaultdict

class Solution:
    def kTop(self,a, n, k):
        #code here.
        ans = []
        mp = defaultdict(int)
        lst = []
        
        for i,v in enumerate(a):
            mp[v] += 1
                
            # new occurence of a element
            if mp[v] == 1:
                lst.append(v)
                
            lst.sort(key=lambda x: (-mp[x], x))
            
            ans.append(lst[: min(k, i + 1)])

        return ans 
        
        
        
        
        
            
            
        
