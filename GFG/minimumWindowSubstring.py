class Solution:

    def smallestWindow(self, s, p):
        # code here
        if (p == "" or len(p) > len(s)):
            return -1
        countMap, window = {}, {}

        for char in p:
            countMap[char] = 1 + countMap.get(char, 0)

        have, need = 0, len(countMap)
        res, resLen = [-1, -1], float("infinity")
        i, j = 0, 0
        while (j < len(s)):
            c = s[j]
            window[c] = 1 + window.get(c, 0)

            if (c in countMap and window[c] == countMap[c]):
                have += 1

            while (have == need):
                # update result
                if (j - i + 1 < resLen):
                    res = [i, j]
                    resLen = j - i + 1

                # pop from left of window
                window[s[i]] -= 1
                if (s[i] in countMap and window[s[i]] < countMap[s[i]]):
                    have -= 1

                i += 1
            j += 1
        i, j = res
        if (resLen != float("infinity")):
            return s[i: j + 1]
        else:
            return -1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        print(ob.smallestWindow(s, p))
