class Solution:
    def trailingZeros(self, N):
        res = 0
        i = 5
        while(i <= N):
            res = res + N//i
            i = i*5
        return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        N = int(input())
        res = Solution().trailingZeros(N)
        print(res)