class Solution:
    def f(self, ind, arr, target, dp):
        if ind == 0:
            if target == 0 and arr[0] == 0:
                return 2

            if target == 0 or arr[0] == target:
                return 1

            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        nottake = self.f(ind - 1, arr, target, dp)
        take = 0

        if arr[ind] <= target:
            take = self.f(ind - 1, arr, target - arr[ind], dp)

        dp[ind][target] = nottake + take
        return dp[ind][target]

    def findTargetSumWays(self, arr, n, target):
        total = sum(arr)

        if (total - target) < 0 or (total - target) % 2 != 0:
            return 0

        target_sum = (total - target) // 2

        dp = [[-1] * (target_sum + 1) for i in range(n)]

        return self.f(n - 1, arr, target_sum, dp)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        res = ob.findTargetSumWays(arr, n, target)
        print(res)