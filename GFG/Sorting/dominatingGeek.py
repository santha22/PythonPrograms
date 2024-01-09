class Solution:
    def minOPs(self, n : int, a : List[int]) -> int:
        # code here
        mp = {}
        for i in a:
            mp[i] = 1 + mp.get(i, 0)
            
        v = []
        for it in mp:
            v.append(mp[it])
        
        v.sort()
        sm , ans = 0, 0
        for i in range(len(v) - 1, -1, -1):
            sm += v[i]
            if sm > n // 2:
                break
            
            ans += 1
        
        return ans
            
