class Solution:
    mod = (10 ** 9) + 7

    def countSubsets(self, pos, currSum, arr, dp):
        if currSum < 0:
            return 0

        if pos == len(arr):
            return 1 if currSum == 0 else 0

        if dp[pos][currSum] != -1:
            return dp[pos][currSum]

        dp[pos][currSum] = (self.countSubsets(pos + 1, currSum, arr, dp) % self.mod +
                            self.countSubsets(pos + 1, currSum - arr[pos], arr, dp) % self.mod) % self.mod

        return dp[pos][currSum]

    def perfectSum(self, arr, n, targetSum):
        dp = [[-1 for j in range(targetSum + 1)] for i in range(n + 1)]
        return self.countSubsets(0, targetSum, arr, dp)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,sum =  input().split()
        n,sum = int(n), int(sum)
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.perfectSum(arr, n, sum)
        print(ans)