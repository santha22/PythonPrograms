def minimumCost(heights, n, k):
    dp = [-1 for i in range(n)]
    dp[0] = 0
    for i in range(1, n):
        minSteps = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                jump = dp[i - j] + abs(heights[i] - heights[i - j])
                minSteps = min(jump, minSteps)

        dp[i] = minSteps

    return dp[n - 1]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = list(map(int, input().split()))
        n,k = a[0], a[1]
        heights = list(map(int, input().split()))
        print(minimumCost(heights, n, k))