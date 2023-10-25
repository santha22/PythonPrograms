class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp = [float("inf")] * n
        
        length = 1
        
        for num in a:
            low, high = 0, length
            
            while low < high:
                mid = (low + high) // 2
                
                if dp[mid] < num:
                    low = mid + 1
                    
                else:
                    high = mid
                    
            dp[low] = num
            
            if low == length:
                length += 1
                
        return length
