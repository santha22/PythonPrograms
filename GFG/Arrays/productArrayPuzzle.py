class Solution:
    def productExceptSelf(self, arr, n):
        #code here
        res = [0] * n
        prefix = 1
        
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
            
        postfix = 1
        
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= arr[i]
            
        return res
