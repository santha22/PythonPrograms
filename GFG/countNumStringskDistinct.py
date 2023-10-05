class Solution:
    def substrCount(self, s, k):
        return self.kMostDistinct(s, k) - self.kMostDistinct(s, k - 1)

    def kMostDistinct(self, s, k):
        n = len(s)
        mp = {}
        res = 0
        i, j = 0, 0
        count = 0

        while j < n:
            mp[s[j]] = 1 + mp.get(s[j], 0)

            if mp[s[j]] == 1:
                count += 1

            while count > k:
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    count -= 1

                i += 1

            res += j - i + 1
            j += 1

        return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        k = int(input())
        ob = Solution()
        res = ob.substrCount(s, k)
        print(res)