class Solution:
    mod = 10 ** 9 + 7

    def f(self, ind, cursum, arr, dp):
        if ind == 0:
            if cursum == 0 and arr[0] == 0:
                return 2

            if cursum == 0 or arr[0] == cursum:
                return 1

            return 0

        if dp[ind][cursum] != -1:
            return dp[ind][cursum]

        nottake = self.f(ind - 1, cursum, arr, dp)

        take = 0
        if arr[ind] <= cursum:
            take = self.f(ind - 1, cursum - arr[ind], arr, dp)

        dp[ind][cursum] = (nottake + take) % self.mod
        return dp[ind][cursum]

    def countPartitions(self, arr, n, d):
        # Code here
        total = sum(arr)

        dp = [[-1] * (total + 1) for i in range(n)]

        if (total - d) < 0 or (total - d) % 2 != 0:
            return 0

        return self.f(n - 1, (total - d) // 2, arr, dp)



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(arr, n, d)
        print(res)