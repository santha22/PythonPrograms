
class Solution:
    def maximumBattalions(self, n : int, names : List[str]) -> int:
        # code here
        mp = {}
        ans = 0
        finish = 0
        
        for i in range(n):
            if names[i] in mp:
                mp[names[i]] = i
                
            else:
                mp[names[i]] = i
                

        for i in range(n):
            finish = max(finish, mp[names[i]])
            
            if finish == i:
                ans += 1
                
        return ans
        
