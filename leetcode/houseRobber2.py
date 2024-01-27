class Solution:
    def f(self, arr):
        n = len(arr)

        prev = arr[0]
        prev2 = 0

        for ind in range(1, n):
            take = arr[ind]
            if ind > 1:
                take += prev2

            nottake = prev

            cur = max(take, nottake)
            prev2 = prev
            prev = cur

        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        temp1 = []
        temp2 = []

        for i in range(n):
            if i != 0:
                temp1.append(nums[i])

            if i != n - 1:
                temp2.append(nums[i])

        return max(self.f(temp1), self.f(temp2))
        
