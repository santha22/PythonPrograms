class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1 for i in range(n)]

        dp[0] = 0

        for i in range(1, n):
            left = dp[i - 1] + abs(height[i] - height[i - 1])
            right = float("inf")

            if i > 1:
                right = dp[i - 2] + abs(height[i] - height[i - 2])

            dp[i] = min(left, right)

        return dp[n - 1]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))