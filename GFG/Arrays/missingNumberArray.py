class Solution:
    def missingNumber(self,array,n):
        # code here
        ans = n * (n + 1) // 2
        sm = 0
        for i in array:
            sm += i
            
        return ans - sm
