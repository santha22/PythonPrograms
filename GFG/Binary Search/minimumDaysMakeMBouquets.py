class Solution:
        
    def f(self, arr, n, mid, m, k):
        count = 0
        total = 0
        for i in range(n):
            if arr[i] <= mid:
                count += 1
            else:
                total += (count // k)
                count = 0

        total += (count // k)
        return total >= m
    
    def solve(self, m, k, arr):
        # Code here
        n = len(arr)  
        val = m * k
        if val > n:
            return -1

        l, h = min(arr), max(arr)
        while l <= h:
            mid = (l + h) // 2

            if self.f(arr, n, mid, m, k):
                h = mid - 1
            else:
                l = mid + 1

        return l
