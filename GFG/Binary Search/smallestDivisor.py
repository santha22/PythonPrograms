import math
class Solution:
    
    def threshold(self, nums, mid, n, k):
        ans = 0
        for i in range(n):
            ans += math.ceil(nums[i] / mid)
            
        return ans <= k

    def smallestDivisor(self, nums, k):
        n = len(nums)
        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            
            if self.threshold(nums, mid, n, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
