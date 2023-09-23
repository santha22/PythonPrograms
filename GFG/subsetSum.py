class Solution:
    def isSubsetSum(self, n, arr, sum):
        dp = [[False] * (sum + 1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, sum + 1):

                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i -1][j] or dp[i - 1][j - arr[i - 1]]

        return dp[n][sum]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sum = int(input())
        ob = Solution()
        if ob.isSubsetSum(n,arr, sum) == True:
            print(1)
        else:
            print(0)