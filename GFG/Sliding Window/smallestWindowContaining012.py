
class Solution:
    def smallestSubstring(self, s):
        # Code here
        mp = {}
        length = float("inf") 
        i,j = 0,0
        
        while j < len(s):
            mp[s[j]] = 1 + mp.get(s[j],  0)
            
            while len(mp) == 3 and i < len(s):
                length = min(length, j - i + 1)
                
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    mp.pop(s[i])
                    
                i += 1
                
            j += 1
                
        
        return length if length != float("inf") else -1

