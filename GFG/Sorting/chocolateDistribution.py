class Solution:

    def findMinDiff(self, arr, n, m):

        # code here
        arr.sort() 
        ans = float("inf")
        i = 0
        while i < n - m + 1:
            j = i + m - 1
            ans = min(ans, arr[j] - arr[i])
            i += 1
            
        return ans
