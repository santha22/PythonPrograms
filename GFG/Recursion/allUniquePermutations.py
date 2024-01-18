
class Solution:
    def recur(self, ans, ds, freq, arr):
        if len(ds) == len(arr):
            ans.append(ds.copy())
            return 
        
        for i in range(len(arr)):
            if freq[i] == 0:
                ds.append(arr[i])
                freq[i] = 1
                self.recur(ans, ds, freq, arr)
                freq[i] = 0
                ds.pop()
                
                
    
    def uniquePerms(self, arr, n):
        # code here 
        ans = []
        ds = []
        freq = [0] * n
        self.recur(ans, ds, freq, arr)
        
        ans = list(set(map(tuple, ans)))
        ans.sort()
        
        return ans
