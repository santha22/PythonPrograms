class Solution:
    def longestOnes(self, n, a, k):
        # Code here
        i,j = 0, 0
        flips = 0
        length = 0
        while i < n and j < n:
            if a[i] == 0:
                    flips += 1
                    
            if flips <= k:
                
                length = max(length, i - j + 1)
                i += 1
            
            else:
                while flips > k:
                    if a[j] == 0:
                        flips -= 1
                    j += 1
                    
                i += 1
                
        return length
