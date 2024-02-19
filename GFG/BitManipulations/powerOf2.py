class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n : int ) -> bool:
        ##Your code here
        if n == 1:
            return True
            
        if n % 2 != 0:
            return False
            
        if n == 0:
            return False
            
        return self.isPowerofTwo(n // 2)
