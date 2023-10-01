class Solution:
    def maximumPath(self, n, matrix):
        # code here
        dp = [[0] * n for i in range(n)]

        for j in range(n):
            dp[n - 1][j] = matrix[n - 1][j]

        for i in range(n - 2, -1, -1):
            for j in range(n):

                d = matrix[i][j] + dp[i + 1][j]
                if j > 0:
                    ld = matrix[i][j] + dp[i + 1][j - 1]
                else:
                    ld = 0
                if j < n - 1:
                    rd = matrix[i][j] + dp[i + 1][j + 1]
                else:
                    rd = 0

                dp[i][j] = max(d, ld, rd)

        return max(dp[0])

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input)
        arr = input().split()
        matrix = [[0]*n for i in range(n)]
        for itr in range(n*n):
            matrix[(itr//n)][itr%n] = int(arr[itr])

        ob = Solution()
        print(ob.maximumPath(n, matrix))