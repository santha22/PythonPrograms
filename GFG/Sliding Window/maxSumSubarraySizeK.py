class Solution:
    def maximumSumSubarray (self, k, arr, n):
        # code here
        i,j = 0,0
        val = 0
        maxi = float("-inf")
        sm = 0
        while j < n:
            sm += arr[j]
            while j - i + 1 > k:
                sm -= arr[i]
                i += 1
                
            maxi = max(maxi, sm)
            j += 1
            
        return maxi
                    
