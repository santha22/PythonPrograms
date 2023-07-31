class Solution:
    def lcs(self, x, y, s1, s2):
        dp = [[0]*(y+1) for i in range(x+1)]
        for i in range(x+1):
            dp[i][0] = 0
        for j in range(y+1):
            dp[0][j] = 0
        for i in range(x+1):
            for j in range(y+1):
                if(s1[i-1]==s2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[x][y]

if __name__ == "__main__":
    t = int(input())
    for t in range(t):
        x,y = map(int,input().split())
        s1 = str(input())
        s2 = str(input())
        ob = Solution()
        print(ob.lcs(x,y,s1,s2))