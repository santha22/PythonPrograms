#User function Template for python3

class Solution:
    def isPossible(self, n, arr):
        # code here 
        ans = 0 
        for i in range(n):
            ans += int(arr[i]) 
        
        if ans % 3 == 0:
            return 1
           
        else: 
            return 0
