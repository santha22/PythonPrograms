class Solution:
    def solve(self, nums, n, k):
        l,c,total = 0,0,0
        for r in range(n):
            if nums[r] % 2 != 0:
                c += 1
                
            while c > k:
                if nums[l] % 2 != 0:
                    c -= 1
                    
                l += 1
                
            total += r - l + 1
            
        return total
    
    def countSubarray(self, n, nums, k):
        # Code here
        return self.solve(nums, n, k) - self.solve(nums, n, k - 1)
