class Solution:
    def distinctSubsequences(self, s):
        mod = 10**9 + 7
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        mp = {}

        for i in range(1, n+1):
            dp[i] = (2 * dp[i-1]) % mod

            curr = s[i - 1]

            if curr in mp:
                dp[i] = (dp[i] - dp[mp[curr] - 1]) % mod

            mp[curr] = i

        return dp[n]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        ans = ob.distinctSubsequences(s)
        print(ans)