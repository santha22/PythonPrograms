class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def choose(self, W, wt, val, n, dp):
        if n <= 0 or W <= 0:
            return 0

        if dp[W][n] != -1:
            return dp[W][n]

        if wt[n - 1] <= W:
            dp[W][n] = max(val[n - 1] + self.choose(W - wt[n - 1], wt, val, n - 1, dp),
                           self.choose(W, wt, val, n - 1, dp))
        else:
            dp[W][n] = self.choose(W, wt, val, n - 1, dp)

        return dp[W][n]

    def knapSack(self, W, wt, val, n):

        # code here
        dp = [[-1 for i in range(n + 1)] for j in range(W + 1)]
        result = self.choose(W, wt, val, n, dp)

        return result
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val, n))
