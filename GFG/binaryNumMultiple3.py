class Solution:
    def isDivisible(self, s):
        binary=int(s,2)
        if binary%3==0:
            return 1
        else:
            return 0

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        ans = ob.isDivisible(s)
        print(ans)