class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
            
        mp = {}
        mp1 = {}
        for c1, c2 in zip(str1, str2):
            if (c1 in mp and mp[c1] != c2) or (c2 in mp1 and mp1[c2] != c1):
                return 0
                
            mp[c1] = c2
            mp1[c2] = c1
            
        return 1
                
