class Solution:
    def romanToDecimal(self, S):
        # code here
        mp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        n = len(S)
        res = 0
        for i in range(n):
            if i + 1 < n and mp[S[i]] < mp[S[i + 1]]:
                res += -mp[S[i]]

            else:
                res += mp[S[i]]

        return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        s = input()
        print(ob.romanToDecimal(s))