class Solution:
    def minPartition(self, n):
        # code here
        arr = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        ans = []
    
        for i in range(len(arr) - 1, -1, -1):
            while n >= arr[i]:
                ans.append(arr[i])
                n = n - arr[i]
    
        return ans
