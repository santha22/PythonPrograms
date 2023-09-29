class Solution:
    def totalWays(self, n, m, grid):
        # Code here
        if grid[0][0] == 1 or grid[n - 1][m - 1]:
            return 0

        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i > 0:
                    dp[i][j] += dp[i - 1][j]

                if j > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[n - 1][m - 1] % (10 ** 9 + 7)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().split())
        grid = []
        for i in range(n):
            col = list(map(int, input().split()))
            grid.append(col)
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
