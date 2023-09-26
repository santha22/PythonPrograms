class Solution:
    def countWays(self, n):
        if n <= 0:
            return 1

        dp = [-1 for i in range(n + 1)]

        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % (10**9 + 7)

        return dp[n]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countWays(n))