class Solution:
    def minOperation(self, n):
        # code here 
        count = 0
        while n:
            if n % 2 == 0:
                n = n // 2
                
            else:
                n = n - 1
                
            count += 1
            
        return count
