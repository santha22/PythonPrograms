class Solution:
    def equalPartition(self, N, arr):
        # code here
        totalSum = sum(arr)

        if totalSum % 2 != 0:
            return False

        curSum = 0
        targetSum = totalSum // 2
        dp = [[None] * (targetSum + 1) for i in range(N + 1)]

        return self.subset(N - 1, arr, curSum, targetSum, dp)

    def subset(self, index, arr, curSum, targetSum, dp):
        if curSum == targetSum:
            return True

        if index < 0 or curSum > targetSum:
            return False

        if dp[index][curSum] != None:
            return dp[index][curSum]

        if arr[index] > targetSum:
            dp[index][curSum] = self.subset(index - 1, arr, curSum, targetSum, dp)

        else:
            dp[index][curSum] = self.subset(index - 1, arr, curSum, targetSum, dp) or self.subset(index - 1, arr,
                                                                                                  curSum + arr[index],
                                                                                                  targetSum, dp)

        return dp[index][curSum]
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        if ob.equalPartition(n, arr) == True:
            print('YES')
        else:
            print('NO')