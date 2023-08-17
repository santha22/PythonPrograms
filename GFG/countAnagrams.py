class Solution:
    def search(self, pat, txt):
        # code here
        if len(pat) > len(txt):
            return 0

        res = []

        pCount, tCount = {}, {}

        for i in range(len(pat)):
            pCount[pat[i]] = 1 + pCount.get(pat[i], 0)
            tCount[txt[i]] = 1 + tCount.get(txt[i], 0)

        if pCount == tCount:
            res = [0]

        i = 0
        for j in range(len(pat), len(txt)):
            tCount[txt[j]] = 1 + tCount.get(txt[j], 0)
            tCount[txt[i]] -= 1

            if tCount[txt[i]] == 0:
                tCount.pop(txt[i])

            i += 1
            if tCount == pCount:
                res.append(i)

        return len(res)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        txt = input()
        pat = input()
        ob = Solution()
        res = ob.search(pat,txt)
        print(res)