class Solution:
    def MinCoin(self, nums, target):
        n = len(nums)

        prev = [0] * (target + 1)

        for T in range(target + 1):
            if T % nums[0] == 0:
                prev[T] = T // nums[0]

            else:
                prev[T] = float("inf")

        for i in range(1, n+1):
            for j in range(target + 1):
                if nums[i - 1] > j:
                    continue

                nottake = prev[j]
                take = 1 + prev[j - nums[i - 1]]
                prev[j] = min(take, nottake)

        if prev[target] >= float("inf"):
            return -1

        return prev[target]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, amount = input().split()
        n = int(n)
        amount = int(amount)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.MinCoin(nums, amount)
        print(ans)