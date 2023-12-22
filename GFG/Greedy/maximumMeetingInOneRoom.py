
        
class Solution:
        
    def maxMeetings(self, n : int, s : List[int], f : List[int]) -> List[int]:
        # code here
        l = []
        for i in range(n):
            l.append([s[i], f[i], i + 1])
            
        l.sort(key = lambda x: x[1])
        
        ans = [l[0][2]]
        last = l[0][1]
        
        
        for i in range(1, n):
            if l[i][0] > last:
                ans.append(l[i][2])
                last = l[i][1]
        
        ans.sort()
        return ans
        
            
